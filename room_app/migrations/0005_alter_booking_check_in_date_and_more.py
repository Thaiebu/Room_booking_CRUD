# Generated by Django 4.1.3 on 2022-11-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_app', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Check_in_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Check_out_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
