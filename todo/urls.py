from django.urls import path
from .import  views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name= 'home'),
    path('detail/<int:pk>',views.detail, name ='detail'),
]