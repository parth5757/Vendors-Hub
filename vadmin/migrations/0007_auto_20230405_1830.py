# Generated by Django 2.2.16 on 2023-04-05 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0006_auto_20230405_1756'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='user',
        ),
    ]
