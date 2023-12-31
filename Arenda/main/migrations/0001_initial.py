# Generated by Django 5.0 on 2023-12-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_arend', models.IntegerField(verbose_name='id дома')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('photo', models.ImageField(upload_to='', verbose_name='фото')),
                ('timees', models.IntegerField(verbose_name='вид времени аренды')),
                ('type_user', models.CharField(max_length=200, verbose_name='кто сдаёт(арендует)')),
                ('type_house', models.CharField(max_length=200, verbose_name='тип сдованмого жилья')),
                ('child', models.IntegerField(verbose_name='можно ли с детьми')),
                ('pet', models.IntegerField(verbose_name='можно ли с животными')),
                ('max_People', models.IntegerField(verbose_name='максимум человек')),
                ('razmer', models.IntegerField(verbose_name='площадь')),
                ('kol_komnat', models.IntegerField(verbose_name='количество комнат')),
                ('adres', models.CharField(max_length=500, verbose_name='Адрес')),
                ('data_obnav', models.TimeField(verbose_name='дата последнего обновления')),
                ('opisanie', models.CharField(max_length=200, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('Email', models.EmailField(max_length=254, verbose_name='Эмэил')),
                ('password', models.CharField(max_length=200, verbose_name='пароль')),
                ('arendhouse', models.IntegerField(verbose_name='id арендованного аренды')),
                ('newarend', models.IntegerField(verbose_name='id выставленного аренды')),
                ('izbran_id', models.IntegerField(verbose_name='id избранный аренд')),
                ('telephone', models.IntegerField(verbose_name='телефон')),
            ],
        ),
    ]
