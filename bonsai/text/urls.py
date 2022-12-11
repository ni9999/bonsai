from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views




urlpatterns = [
    path('', views.extract, name = 'extract'),
    path('options', views.options, name = 'options'),
    path('output', views.output, name = 'output'),
    path('direct', views.direct, name = 'direct'),
]
