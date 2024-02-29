# Generated by Django 5.0.2 on 2024-02-29 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prediction', '0014_alter_predict_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(70)]),
        ),
        migrations.AlterField(
            model_name='predict',
            name='bloodPressure',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(110)]),
        ),
        migrations.AlterField(
            model_name='predict',
            name='bmi',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='predict',
            name='glucose',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='predict',
            name='insulin',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(350)]),
        ),
        migrations.AlterField(
            model_name='predict',
            name='skinThickness',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(85)]),
        ),
    ]
