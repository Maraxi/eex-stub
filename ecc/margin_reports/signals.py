from django.db.models.signals import post_save
from django.dispatch import receiver
from margin_reports.models import EndofDay, Intraday


@receiver(post_save, sender=Intraday)
def check_intraday(sender, **kwargs):
    print("intra")


@receiver(post_save, sender=EndofDay)
def check_startofday(sender, **kwargs):
    print("start")
