# Generated by Django 4.0 on 2021-12-13 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("margin_reports", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MarginClassSurveilance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("SPAN", models.BooleanField()),
                ("IMSM", models.BooleanField()),
                ("CESM", models.BooleanField()),
                ("AMPO", models.BooleanField()),
                ("AMEM", models.BooleanField()),
                ("AMCO", models.BooleanField()),
                ("AMCU", models.BooleanField()),
                ("AMWI", models.BooleanField()),
                ("DMEM", models.BooleanField()),
                (
                    "Account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="margin_reports.account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ErrorEmailRecipients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Recipient", models.CharField(max_length=100)),
                (
                    "Account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="margin_reports.account",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="endofday",
            name="Account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="margin_reports.account"
            ),
        ),
        migrations.AlterField(
            model_name="intraday",
            name="Account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="margin_reports.account"
            ),
        ),
    ]