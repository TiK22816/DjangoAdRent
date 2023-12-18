from django.db import models

class users(models.Model):
    name = models.CharField('Имя',max_length = 200)

    Email = models.EmailField('Эмэил')

    password = models.CharField('пароль',max_length = 200)

    # arendhouse = models.IntegerField('id арендованного аренды', Null=True, blank=True)
    #
    # newarend = models.IntegerField('id выставленного аренды', Null=True, blank=True)
    #
    # izbran_id = models.IntegerField('id избранный аренд', Null=True, blank=True)

    telephone = models.IntegerField('телефон')
    def get_absolute_url(self):
        return '/settings/'




class house(models.Model):
    name = models.CharField('Название обьявления', max_length=50)
    id_User = models.CharField('id пользователя', max_length=200)
    telephone = models.CharField('номер телефона', max_length=12)
    price = models.IntegerField('цена')
    photo1 = models.ImageField('фото', upload_to='static/images',default = "Arenda/static/images/0.jpg")
    photo2 = models.ImageField('фото', upload_to='static/images',default = "Arenda/static/images/0.jpg")
    photo3 = models.ImageField('фото', upload_to='static/images',default = "Arenda/static/images/0.jpg")
    photo4 = models.ImageField('фото', upload_to='static/images',default = "Arenda/static/images/0.jpg")
    times = models.CharField('вид времени аренды', max_length=200, default='Месяц')   # месяц/день
    type_house = models.CharField('тип сдованмого жилья',max_length = 200)
    child = models.CharField('можно ли с детьми', max_length = 200, default='нет')
    pet = models.CharField('можно ли с животными', max_length = 200, default='нет')
    max_People = models.IntegerField('максимум человек')
    razmer = models.IntegerField('площадь')
    kol_komnat = models.IntegerField('количество комнат')
    adres = models.CharField('Адрес',max_length = 200)
    opisanie = models.CharField('описание',blank=True, max_length=200)

class idd(models.Model):
    iddd = models.IntegerField('индекс')