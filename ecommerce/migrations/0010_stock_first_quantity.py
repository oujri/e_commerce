# Generated by Django 2.0.4 on 2018-05-05 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_auto_20180505_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='first_quantity',
            field=models.IntegerField(default=0),
        ),
    ]