# Generated by Django 5.0.6 on 2024-07-02 05:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="diningplace",
            name="endtime",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="diningplace",
            name="starttime",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
