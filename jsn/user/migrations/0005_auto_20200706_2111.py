# Generated by Django 3.0.5 on 2020-07-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200706_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(upload_to='user/images'),
        ),
    ]
