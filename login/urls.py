from django.urls import path
from . import views as login_views

urlpatterns = [
    path('', login_views.home, name='Login Page'),
]