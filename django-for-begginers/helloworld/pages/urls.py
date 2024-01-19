from django.contrib import admin
from django.urls import path
from .views import home_page_view

urlpatterns = [
    path("", view=home_page_view, name="home"),
]
