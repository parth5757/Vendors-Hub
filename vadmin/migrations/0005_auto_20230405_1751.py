# Generated by Django 2.2.16 on 2023-04-05 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0004_auto_20230405_1751'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profile',
            new_name='user',
        ),
    ]
