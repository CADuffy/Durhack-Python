from django.urls import path

from . import views

urlpatterns = [
    path('', views.initialise, name='initialise'),
    path('customer-connect', views.index, name='index'),
    path('waiting', views.waiting, name='waiting'),
    path('front', views.front, name='front'),
    path('company-register', views.company_register, name='company_register'),
    path('nextperson', views.nextperson, name="'nextperson"),
    path('register-company', views.register_company, name="register_company"),
    path('login-company', views.login_company, name="login_company")
]