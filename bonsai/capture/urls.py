from django.contrib import admin
from django.urls import path
from django.urls import include
# from text import views
from . import views




urlpatterns = [
    #display both cameras
    path('', views.index.as_view(), name='index'),
    path('text/', include('text.urls'), name = 'text'),

]
