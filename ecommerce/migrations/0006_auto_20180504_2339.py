# Generated by Django 2.0.4 on 2018-05-04 22:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20180504_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='dateFin',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 22, 39, 52, 522236, tzinfo=utc)),
        ),
    ]
