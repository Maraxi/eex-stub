import logging

from django.core.mail import send_mass_mail
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from margin_reports.models import EndofDay, ErrorEmailRecipients, Intraday


@receiver(post_save, sender=Intraday)
def check_intraday(sender, **kwargs):
    """Check if first CI050 of the day covers extra margins of last CC050 and create error reports."""
    ci050 = kwargs["instance"]

    if not isSurveiled(ci050):
        # Margin Class not marked for checking
        return

    filter_sameday = {
        "Account": ci050.Account,
        "Margin_Class": ci050.Margin_Class,
        "Report_Date": ci050.Report_Date,
    }
    if Intraday.objects.filter(**filter_sameday).count() > 1:
        # This is not the first intraday margin of the day
        return

    filter_previousdays = {
        "Account": ci050.Account,
        "Margin_Class": ci050.Margin_Class,
        "Report_Date__lt": ci050.Report_Date,
    }
    last_cc050 = (
        EndofDay.objects.filter(**filter_previousdays).order_by("Report_Date").last()
    )

    filter_previousday = {
        "Account": ci050.Account,
        "Margin_Class": ci050.Margin_Class,
        "Report_Date": last_cc050.Report_Date,
    }
    sumofpreviousintraday = Intraday.objects.filter(**filter_previousday).aggregate(
        Sum("Margin")
    )["Margin__sum"]

    if ci050.Margin + sumofpreviousintraday < last_cc050:
        message = f"First CI050 report of the day {ci050=} does not cover extra margins of last cc050 report {last_cc050=}"
        handleMarginError(message, ci050.account)


@receiver(post_save, sender=EndofDay)
def check_startofday(sender, **kwargs):
    """Check if CC050 covers Margins of CI050 reports of current day and create error reports."""
    cc050 = kwargs["instance"]

    if not isSurveiled(cc050):
        # Margin Class not marked for checking
        return

    intraday_entries = Intraday.objects.filter(
        Account=cc050.Account,
        Margin_Class=cc050.Margin_Class,
        Report_Date=cc050.Report_Date,
    )
    if intraday_entries.aggregate(Sum("Margin"))["Margin__sum"] > cc050.Margin:
        message = f"CC050 report of the day {cc050=} does not cover margins of the current day {intraday_entries=}"
        handleMarginError(message, cc050.account)


def isSurveiled(report):
    """Look up serveilance in the MarginClassSurveilance table."""
    surveilance = report.account.marginclasssurveilance
    return surveilance.__getattribute__(report.Margin_Class)


def handleMarginError(message, account):
    logger = logging.getLogger("MarginLogger")
    logger.error(message)

    targets = ErrorEmailRecipients.objects.filter(Account=account)
    datatuple = (
        ("MarginError", message, "margin_checker@exx.com", target) for target in targets
    )
    send_mass_mail(datatuple)
