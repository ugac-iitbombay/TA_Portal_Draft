from django.urls import path
from . import views as faculty_views

urlpatterns = [
    path('', faculty_views.home, name='Faculty-Home'),
    path('add_course/', faculty_views.add_course, name='Add Course'),
    path('course/', faculty_views.course, name='Applications for course'),
    path('course/student/', faculty_views.student, name='Student Profile'),
    path('course/mail/', faculty_views.mail, name='Mail students'),
]
