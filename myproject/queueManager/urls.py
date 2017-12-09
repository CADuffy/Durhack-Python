from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('waiting', views.waiting, name='waiting'),
    path('front', views.front, name='front')
]