# Generated by Django 4.0 on 2021-12-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("margin_reports", "0004_alter_marginclasssurveilance_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="AMCO",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="AMCU",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="AMEM",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="AMPO",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="AMWI",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="CESM",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="DMEM",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="IMSM",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="marginclasssurveilance",
            name="SPAN",
            field=models.BooleanField(default=True),
        ),
    ]