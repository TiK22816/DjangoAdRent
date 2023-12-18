from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.glavnaya, name='glavnaya'),

    path('register/', views.register, name='register'),

    path('pastethepost/', views.pastethepost, name='pastethepost'),

    path('kabinet/', views.kabinet, name='kabinet'),

    path('login/', views.login, name='login'),

    path('lobby/', views.glavnaya1, name='glavnaya 1'),

    path('password/<int:pk>', views.password.as_view(), name='password'),

    path('logins/', views.logins, name='logins'),

    path('number/<int:pk>', views.number.as_view(), name='number'),

    path('Email/<int:pk>', views.Email.as_view(), name='Email'),

    path('settings/', views.settings, name='settings'),

    path('newarend/', views.newarend, name='newarend'),

    path('my_arend/', views.my_arend, name='my_arend'),

    path('arendy/<int:pk>', views.arendy, name='arendy'),

]