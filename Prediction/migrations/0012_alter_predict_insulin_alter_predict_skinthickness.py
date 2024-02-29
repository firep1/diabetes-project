# Generated by Django 4.2.7 on 2024-02-28 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prediction", "0011_predict_bloodpressure_alter_predict_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predict",
            name="insulin",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(10),
                    django.core.validators.MaxValueValidator(350),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="skinThickness",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(5),
                    django.core.validators.MaxValueValidator(85),
                ]
            ),
        ),
    ]