from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profiles_db', views.profiles_db, name="profiles_db"),
]