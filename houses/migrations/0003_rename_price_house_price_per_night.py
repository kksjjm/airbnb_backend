# Generated by Django 4.2.5 on 2023-09-26 13:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("houses", "0002_rename_prince_house_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="house",
            old_name="price",
            new_name="price_per_night",
        ),
    ]
