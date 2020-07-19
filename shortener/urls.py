from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import HomeView, kirrCBView

urlpatterns = [

    url(r'^$', HomeView.as_view()),
]
