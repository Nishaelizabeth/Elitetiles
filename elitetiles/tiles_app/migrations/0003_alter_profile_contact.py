# Generated by Django 5.1.2 on 2024-11-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles_app', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]