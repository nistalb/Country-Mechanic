# Generated by Django 3.1.6 on 2021-02-05 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='hours',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='mileage',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]