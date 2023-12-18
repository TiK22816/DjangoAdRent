from .models import users, house, idd
from django.forms import ModelForm, TextInput, FileInput, NumberInput, Textarea

class UserForm(ModelForm):
    class Meta:
        model = users
        fields = ['name',
                  'Email',
                  'password',
                  'telephone']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }),
            'telephone': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
            }),
            'Email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }),
        }
class HouseForm(ModelForm):
    class Meta:
        model = house
        fields = ['price',
                  'name',
                  'photo1',
                  'photo2',
                  'photo3',
                  'photo4',
                  'type_house',
                  'max_People',
                  'razmer',
                  'kol_komnat',
                  'adres',
                  'opisanie',
                  'id_User',
                  'telephone',
                  'times',
                  'child',
                  'pet',
                  ]
        widgets = {
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',}),

            'photo1': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Переместите сюда фото',}),

            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название обьявления', }),

            'photo2': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Переместите сюда фото',}),
            'photo3': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Переместите сюда фото',}),
            'photo4': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Переместите сюда фото',}),

            'type_house': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип сдаваемого помещения', }),

            'max_People': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Максимум человек', }),

            'razmer': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Площадь сдаваемого помещения', }),

            'kol_komnat': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество комнат', }),

            'adres': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес', }),

            'opisanie': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание', }),

            'id_User': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя', }),

            'telephone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваши контакты',}),

            'times': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'За какой промежуток времени указана цена', }),

            'child': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Можно ли с детьми', }),

            'pet': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Можно ли с животными', }),
        }
class iddForm(ModelForm):
    class Meta:
        model = idd
        fields = ['iddd']
