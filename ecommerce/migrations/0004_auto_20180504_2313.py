# Generated by Django 2.0.4 on 2018-05-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20180504_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='dateFin',
            field=models.DateTimeField(),
        ),
    ]
