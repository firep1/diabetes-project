# Generated by Django 4.2.7 on 2023-11-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prediction", "0005_alter_predict_bmi_alter_predict_insulin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predict",
            name="age",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="predict",
            name="diabetesPedigree",
            field=models.FloatField(),
        ),
    ]
