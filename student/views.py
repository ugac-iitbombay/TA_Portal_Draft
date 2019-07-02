from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'student/home.html')

def my_applications(request):
    return render(request, 'student/my_applications.html')

def profile(request):
    return render(request, 'student/profile.html')

def apply(request):
    return render(request, 'student/apply.html')

