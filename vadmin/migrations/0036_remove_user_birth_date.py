# Generated by Django 3.2.5 on 2023-05-04 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0035_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
    ]
