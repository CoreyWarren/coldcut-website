from django.contrib import admin
from . import views
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name='index'),

]