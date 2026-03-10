from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
   # path('', views.post_list, name='post_list'),
   path('portao', views.portao),
   path('sala', views.sala),
   path('quarto', views.quarto),
   path('post_list', views.post_list),
  
]
