from django.urls import path
from . import views as student_views

urlpatterns = [
    path('', student_views.home, name='Student-Home'),
    path('my_applications/', student_views.my_applications, name='My Applications'),
    path('profile/', student_views.profile, name='My Profile'),
    path('apply/', student_views.apply, name='Apply'),
]
