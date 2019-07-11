from django.urls import path, include
from . import views as login_views
from django.contrib.auth import views as auth_views
"""from login.forms import LoginForm"""

urlpatterns = [
    path('', login_views.home, name='Login Page'),
    path('post/', login_views.post),
]