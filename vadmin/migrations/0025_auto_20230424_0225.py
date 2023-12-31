# Generated by Django 3.2.5 on 2023-04-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0024_auto_20230424_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.DeleteModel(
            name='P_Category',
        ),
    ]
