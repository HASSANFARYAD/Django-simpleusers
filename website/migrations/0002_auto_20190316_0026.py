# Generated by Django 2.1.7 on 2019-03-15 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
