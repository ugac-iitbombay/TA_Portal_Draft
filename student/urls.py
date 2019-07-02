from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Student-Home'),
    path('my_applications/', views.my_applications, name='My Applications'),
    path('profile/', views.profile, name='My Profile'),
    path('apply/', views.apply, name='Apply'),
]
