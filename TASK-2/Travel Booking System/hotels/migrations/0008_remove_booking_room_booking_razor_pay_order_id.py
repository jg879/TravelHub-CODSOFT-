# Generated by Django 4.2.4 on 2023-08-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_room_check_in_date_room_check_out_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.AddField(
            model_name='booking',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
