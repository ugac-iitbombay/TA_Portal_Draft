from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Faculty-Home'),
    path('add_course/', views.add_course, name='Add Course'),
    path('course/', views.course, name='Applications for course'),
    path('course/student/', views.student, name='Student Profile'),
    path('course/mail/', views.mail, name='Mail students'),
]
