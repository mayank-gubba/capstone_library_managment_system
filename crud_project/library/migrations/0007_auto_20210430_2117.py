# Generated by Django 3.1.5 on 2021-04-30 15:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20210430_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=40), null=True, size=3),
        ),
    ]
