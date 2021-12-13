from django.db import models


class Account(models.Model):
    Name = models.CharField(max_length=100)


class Intraday(models.Model):
    Clearing_Member = models.CharField(max_length=100)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Margin_Class = models.CharField(max_length=20)
    Margin = models.DecimalField(decimal_places=3, max_digits=13)
    Report_Date = models.DateField()
    Report_Time = models.TimeField()


class EndofDay(models.Model):
    Clearing_Member = models.CharField(max_length=100)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Margin_Class = models.CharField(max_length=20)
    Margin = models.DecimalField(decimal_places=3, max_digits=13)
    Report_Date = models.DateField()


class MarginClassSurveilance(models.Model):
    Account = models.OneToOneField(Account, on_delete=models.CASCADE)
    SPAN = models.BooleanField(default=True)
    IMSM = models.BooleanField(default=True)
    CESM = models.BooleanField(default=True)
    AMPO = models.BooleanField(default=True)
    AMEM = models.BooleanField(default=True)
    AMCO = models.BooleanField(default=True)
    AMCU = models.BooleanField(default=True)
    AMWI = models.BooleanField(default=True)
    DMEM = models.BooleanField(default=True)


class ErrorEmailRecipients(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Recipient = models.CharField(max_length=100)
