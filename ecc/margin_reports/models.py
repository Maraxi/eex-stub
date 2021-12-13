from django.db import models


class Account(models.Model):
    Name = models.CharField(max_length=100)


class Intraday(models.Model):
    Clearing_Member = models.CharField(max_length=100)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Margin_Class = models.CharField(max_length=20)
    Margin = models.DecimalField(decimal_places=3, max_digits=13)
    Report_Date = models.DateField()


class EndofDay(models.Model):
    Clearing_Member = models.CharField(max_length=100)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Margin_Class = models.CharField(max_length=20)
    Margin = models.DecimalField(decimal_places=3, max_digits=13)
    Report_Date = models.DateField()
    Report_Time = models.TimeField()


class MarginClassSurveilance(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    SPAN = models.BooleanField()
    IMSM = models.BooleanField()
    CESM = models.BooleanField()
    AMPO = models.BooleanField()
    AMEM = models.BooleanField()
    AMCO = models.BooleanField()
    AMCU = models.BooleanField()
    AMWI = models.BooleanField()
    DMEM = models.BooleanField()


class ErrorEmailRecipients(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Recipient = models.CharField(max_length=100)
