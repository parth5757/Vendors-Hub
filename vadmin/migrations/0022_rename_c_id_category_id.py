# Generated by Django 3.2.5 on 2023-04-23 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0021_auto_20230424_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='c_id',
            new_name='id',
        ),
    ]