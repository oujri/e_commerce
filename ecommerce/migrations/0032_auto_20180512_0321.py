# Generated by Django 2.0.4 on 2018-05-12 02:21

from django.db import migrations, models
import django.db.models.deletion
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0031_auto_20180511_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, upload_to=ecommerce.models.PathAndRename('images/2018/05/12')),
        ),
        migrations.AlterField(
            model_name='commercecategory',
            name='image',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/12')),
        ),
        migrations.AlterField(
            model_name='commerceimage',
            name='image',
            field=models.ImageField(upload_to=ecommerce.models.PathAndRename('images/2018/05/12')),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/12')),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to=ecommerce.models.PathAndRename('slides/2018/05/12')),
        ),
        migrations.AddField(
            model_name='description',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Product'),
        ),
    ]
