# Generated by Django 5.0 on 2023-12-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
    ]
