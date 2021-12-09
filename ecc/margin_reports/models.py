from django.db import models

# Create your models here.


class Intraday(models.Model):
    Clearing_Member = models.CharField(max_length=100)
    Account = models.CharField(max_length=40)
    Margin_Class = models.CharField(max_length=20)
    Margin = models.DecimalField(decimal_places=3, max_digits=13)
    Report_Date = models.DateField()


class EndofDay(models.Model):
    Clearing_Member = models.CharField(max_length=100)
    Account = models.CharField(max_length=40)
    Margin_Class = models.CharField(max_length=20)
    Margin = models.DecimalField(decimal_places=3, max_digits=13)
    Report_Date = models.DateField()
    Report_Time = models.TimeField()
