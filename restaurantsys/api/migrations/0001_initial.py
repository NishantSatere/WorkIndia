# Generated by Django 5.0.6 on 2024-07-02 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="admin",
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
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="startandentime",
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
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="DiningPlace",
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
                ("name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("phone_no", models.CharField(max_length=15)),
                ("website", models.URLField()),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.admin"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DiningPlaceOperatingHours",
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
                ("open_time", models.TimeField()),
                ("close_time", models.TimeField()),
                (
                    "dining_place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.diningplace",
                    ),
                ),
                (
                    "operational_hours",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.startandentime",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="diningplace",
            name="operational_hours",
            field=models.ManyToManyField(
                through="api.DiningPlaceOperatingHours", to="api.startandentime"
            ),
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("booking_time", models.DateTimeField(auto_now_add=True)),
                (
                    "dining_place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.diningplace",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user"
                    ),
                ),
            ],
        ),
    ]
