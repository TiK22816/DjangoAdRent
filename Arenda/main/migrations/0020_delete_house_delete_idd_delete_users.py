# Generated by Django 5.0 on 2023-12-16 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_house_child_house_pet_house_times'),
    ]

    operations = [
        migrations.DeleteModel(
            name='house',
        ),
        migrations.DeleteModel(
            name='idd',
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
