# Generated by Django 4.2.4 on 2023-08-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_remove_room_check_in_date_remove_room_check_out_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='check_in_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='check_out_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
