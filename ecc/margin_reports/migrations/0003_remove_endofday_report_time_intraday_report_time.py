# Generated by Django 4.0 on 2021-12-13 11:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "margin_reports",
            "0002_account_marginclasssurveilance_erroremailrecipients_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="endofday",
            name="Report_Time",
        ),
        migrations.AddField(
            model_name="intraday",
            name="Report_Time",
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
