# Generated by Django 4.2.5 on 2023-10-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medias", "0002_remove_photo_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="name",
        ),
        migrations.AddField(
            model_name="video",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="photo",
            name="descriptions",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="video",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
