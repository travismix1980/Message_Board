# Generated by Django 5.1.2 on 2024-11-20 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Post",
        ),
    ]
