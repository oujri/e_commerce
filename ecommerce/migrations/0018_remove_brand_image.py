# Generated by Django 2.0.4 on 2018-05-06 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0017_brand_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='image',
        ),
    ]
