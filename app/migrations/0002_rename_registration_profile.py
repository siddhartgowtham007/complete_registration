# Generated by Django 4.2.7 on 2024-01-26 06:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registration',
            new_name='profile',
        ),
    ]
