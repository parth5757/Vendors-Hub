# Generated by Django 3.2.5 on 2023-04-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0020_delete_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='c_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]