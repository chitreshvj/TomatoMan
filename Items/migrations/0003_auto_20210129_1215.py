# Generated by Django 3.1.5 on 2021-01-29 06:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_auto_20210129_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetails',
            name='status',
            field=models.CharField(choices=[(' ', ' In stock'), ('Out Of Stock', 'out of stock')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 29, 6, 45, 23, 940761, tzinfo=utc), verbose_name='date published'),
        ),
    ]
