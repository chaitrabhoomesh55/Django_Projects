from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='index'), 
    path('<int: domain_id/', views.training_domain, name='domain'),
    path('', views.home, name='home'),
    path('about/', views.about),
    path('register', views.create, name='register'),
    path('success', views.success, name='success'),
    path('json/', views.random, name='json'),
    path('api/', views.Registerlist.as_view()),
    
]

