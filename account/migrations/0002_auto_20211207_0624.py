# Generated by Django 3.1 on 2021-12-07 00:24

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', account.models.MyUserManager()),
            ],
        ),
    ]
