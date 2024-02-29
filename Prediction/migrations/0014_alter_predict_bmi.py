# Generated by Django 5.0.2 on 2024-02-29 18:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prediction', '0013_alter_predict_age_alter_predict_bloodpressure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='bmi',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(60)]),
        ),
    ]