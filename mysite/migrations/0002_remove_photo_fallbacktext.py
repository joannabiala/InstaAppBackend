# Generated by Django 2.2.7 on 2020-02-14 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='fallbackText',
        ),
    ]