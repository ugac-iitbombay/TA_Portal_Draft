from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'faculty/home.html')

def add_course(request):
    return render(request, 'faculty/add_course.html')

def course(request):
    return render(request, 'faculty/course.html')

def student(request):
    return render(request, 'faculty/student.html')

def mail(request):
    return render(request, 'faculty/mail.html')