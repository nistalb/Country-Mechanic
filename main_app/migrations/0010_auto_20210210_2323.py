# Generated by Django 3.1.6 on 2021-02-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210210_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='video',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
