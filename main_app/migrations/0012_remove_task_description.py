# Generated by Django 3.1.6 on 2021-02-10 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210210_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
