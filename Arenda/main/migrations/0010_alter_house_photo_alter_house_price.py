# Generated by Django 5.0 on 2023-12-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_house_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.IntegerField(verbose_name='цена'),
        ),
    ]
