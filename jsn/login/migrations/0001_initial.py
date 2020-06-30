# Generated by Django 3.0.5 on 2020-06-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('emailid', models.EmailField(default=None, max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('activeotp', models.BooleanField(default=False)),
                ('lastlogin', models.CharField(max_length=30)),
                ('otp', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
    ]
