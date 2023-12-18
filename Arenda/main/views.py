from django.shortcuts import render,HttpResponseRedirect
from .forms import UserForm, HouseForm, iddForm
from .models import users, house, idd
from django.views.generic import UpdateView, DeleteView, ListView


class password(UpdateView):
    model = users
    template_name = ('password.html')
    fields = ['password']





class number(UpdateView):
    model = users
    template_name = ('number.html')
    fields = ['telephone']




class Email(UpdateView):
    model = users
    template_name = ('Email.html')
    fields = ['Email']





def logins(request):
    error = ''
    iddobject = idd.objects.all()
    for i in iddobject:
        iidd = i.iddd
    on = True
    user = users.objects.get(id=iidd)
    userses = users.objects.all()
    if request.method == 'POST':
        i = {
            'name': request.POST['name'],
            'password': user.password,
            'Email': user.Email,
            'telephone': user.telephone
        }
        form = UserForm(i)
        if form.is_valid():
            for el in userses:
                if request.POST['name'] == el.name:
                    error = 'Такой логин уже есть'
                    on = False
                    break
            if on == True:
                user.name = request.POST['name']
                user.save(update_fields=["name"])
                data = {
                    'idd': iidd,
                    'form': form,
                }
                return render(request, 'settings.html', data)
        else:
            error = 'Некоректно введены данные'
    else:
        f = {
            'name': user.name,
            'password': user.password,
            'Email': user.Email,
            'telephone': user.telephone
        }
        form = UserForm(f)
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'logins.html', data)




def kabinet(request):
    return render(request, 'kabinet.html')

def my_arend(request):
    error = ''
    user = users.objects.all()
    houses = house.objects.all()
    iddobject = idd.objects.all()
    for i in iddobject:
        iidd = i.iddd
    if request.method == 'POST':
        form = HouseForm(request.POST)
        f = 1
        for el in houses:
            if request.POST['adres'] == el.adres and el.id_User == str(iidd):
                House = el
                House.delete()
                data = {
                    'user': user,
                    'house': houses,
                }
                return render(request, 'my_arend.html', data)
            else:
                error = 'Неверный адрес или этот объект вам не принадлежит'
        f += 1
    else:
        form = HouseForm()
    data = {
        'user': user,
        'form':form,
        'house': houses,
        'iidd':  str(iidd),
        'error': error,
    }
    return render(request, 'my_arend.html', data)


def glavnaya(request):
    user = users.objects.all()
    houses = house.objects.all()
    form = iddForm()
    if request.method == 'POST':
        data = {
            'user': user,
            'house': houses,
            'form': form,
        }
        return render(request, 'glavnaya poisk.html', data)

    data = {
        'user': user,
        'house': houses,
        'form': form
    }
    return render(request, 'glavnaya.html', data)


def newarend(request):
    user = users.objects.all()
    houses = house.objects.all()
    iddobject = idd.objects.all()
    for i in iddobject:
        iidd = i.iddd
    error = ''
    if request.method == 'POST':
        i = dict(request.POST)
        i['id_User'] = iidd
        i['name'] = i['name'][0]
        i['telephone'] = i['telephone'][0]
        i['csrfmiddlewaretoken'] = i['csrfmiddlewaretoken'][0]
        i['price'] = i['price'][0]
        i['type_house'] = i['type_house'][0]
        i['max_People'] = i['max_People'][0]
        i['razmer'] = i['razmer'][0]
        i['kol_komnat'] = i['kol_komnat'][0]
        i['adres'] = i['adres'][0]
        i['opisanie'] = i['opisanie'][0]
        i['times'] = i['times'][0]
        i['child'] = i['child'][0]
        i['pet'] = i['pet'][0]
        form = HouseForm(i, request.FILES)
        if form.is_valid():
            form.save()
            data = {
                'user': user,
                'house': houses,
            }
            return render(request, 'glavnaya 1.html', data )

        else:
            error = 'Некоректно введены данные'

    else:
        form = HouseForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'newarend.html', data)

def arendy(request, pk):
    houses = house.objects.get(id=pk)
    user = users.objects.get(id=houses.id_User)
    data = {
        'user': user,
        'house': houses,
    }
    return render(request, 'arendy.html', data)


def login(request):
    error = ''
    idd = 0
    user = users.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        error = 'Неправельный логин или пароль'
        for el in user:
            if request.POST['name'] == el.name and request.POST['password'] == el.password:
                idd = el.id
                iid = {"iddd": idd}
                i = iddForm(iid)
                i.save()
                return render(request, 'kabinet.html')
    else:
        form = UserForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'login.html', data)






def settings(request):
    iddobject = idd.objects.all()
    for i in iddobject:
        iidd = i.iddd
    form = UserForm()
    data = {
        'idd': iidd,
        'form': form,
    }
    return render(request, 'settings.html', data )




def glavnaya1(request):
    user = users.objects.all()
    houses = house.objects.all()
    data = {
        'user': user,
        'house': houses,
    }
    return render(request, 'glavnaya 1.html',data)






def pastethepost(request):
    return render(request, 'pastethepost.html')






def register(request):
    error = ''
    on = True
    user = users.objects.all()
    houses = house.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            for el in user:
                if request.POST['name'] == el.name:
                    error = 'Такой логин уже есть'
                    on = False
                    break
            if on == True:
                form.save()
                data = {
                    'user': user,
                    'house': houses,
                }
                return render(request, 'glavnaya.html', data)
        else:
            error = 'Некоректно введены данные'
    else:
        form = UserForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'register.html', data)


