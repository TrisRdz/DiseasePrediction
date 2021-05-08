from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.usrcr, name='usrcr'),
    path('', views.log, name='log'),
    path('loging/', views.loging, name='loging'),
    path('loging/delet', views.delete_user, name='delete_user'),
    path('sign/', views.sgn, name='sgn'),

    path('pred/', views.sel, name='sel'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('find/', views.find, name='find'),
    path('sign0/', views.sgn4, name='sgn4'),
    path('Hospitals/', views.Hospitals, name='Hospitals'),
    path('ff/', views.ff, name='ff'),
    # path('sign1/', views.sgn2, name='sgn2'),
    path('sign0/', views.sgn4, name='sgn4'),
    path('sign2/', views.sgn3, name='sgn3'),
    path('', views.sgn, name='sgn0'),
    path('sign1/', views.sgn2, name='sgn2'),

]
