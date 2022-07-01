from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings


urlpatterns = [

    path('', views.main, name='main'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]