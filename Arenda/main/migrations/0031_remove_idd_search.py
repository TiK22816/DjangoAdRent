# Generated by Django 4.1.7 on 2023-12-17 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_idd_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idd',
            name='search',
        ),
    ]
