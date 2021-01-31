# Generated by Django 3.1.5 on 2021-01-29 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_auto_20210129_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='total',
            new_name='total_amount',
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 29, 10, 2, 42, 819725, tzinfo=utc), verbose_name='date published'),
        ),
    ]
