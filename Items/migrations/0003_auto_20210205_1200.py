# Generated by Django 3.1.5 on 2021-02-05 06:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_auto_20210201_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 6, 29, 59, 927606, tzinfo=utc), verbose_name='date published'),
        ),
    ]
