# Generated by Django 5.0 on 2023-12-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_house_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='id_User',
            field=models.IntegerField(default=0, verbose_name='id пользователя'),
        ),
    ]
