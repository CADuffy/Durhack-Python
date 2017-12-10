from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('waiting', views.waiting, name='waiting'),
    path('front', views.front, name='front'),
    path('company', views.company, name='company'),
    path('nextperson', views.nextperson, name="'nextperson")
]