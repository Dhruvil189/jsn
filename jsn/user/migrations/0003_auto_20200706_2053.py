# Generated by Django 3.0.5 on 2020-07-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200706_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(upload_to='media/user/images'),
        ),
    ]
