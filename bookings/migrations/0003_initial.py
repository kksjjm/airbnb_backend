# Generated by Django 4.2.5 on 2023-10-04 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rooms", "0001_initial"),
        ("bookings", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rooms.room",
            ),
        ),
    ]
