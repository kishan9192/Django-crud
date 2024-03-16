from django.urls import path
from . import views

#this variable will be of this name only
urlpatterns = [
    path('hello/', views.say_hello),
    path('drinks/', views.drink_list),
    path('drinks/<int:id>/', views.drink_detail)
]