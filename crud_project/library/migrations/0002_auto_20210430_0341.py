# Generated by Django 3.1.5 on 2021-04-29 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bid',
            new_name='isbn',
        ),
    ]
