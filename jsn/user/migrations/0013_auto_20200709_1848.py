# Generated by Django 3.0.5 on 2020-07-09 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200709_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 9, 18, 48, 17, 826679)),
        ),
    ]
