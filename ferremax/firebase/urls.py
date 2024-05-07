from django.contrib import admin
from django.urls import path, include

from firebase import views

urlpatterns = [
    path('', views.firebase, name="firebase"),
]