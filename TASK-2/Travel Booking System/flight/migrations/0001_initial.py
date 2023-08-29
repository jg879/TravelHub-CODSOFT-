# Generated by Django 4.2.4 on 2023-08-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('airport', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=3)),
                ('country', models.CharField(max_length=64)),
            ],
        ),
    ]
