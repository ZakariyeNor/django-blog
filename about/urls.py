from django.urls import path
from . import views

#create url 
urlpatterns = [
    path('', views.about_me, name='about')
]