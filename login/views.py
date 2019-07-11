from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from login.forms import LoginForm

def home(request):
    form = LoginForm()
    return render(request, 'login/home.html', {'form' : form})
    
    def get(request):
        form = LoginForm()
        return render(request, 'login/home.html', {'form' : form})

def post(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        ldap = form.cleaned_data['ldap']
        password = form.cleaned_data['password']
        if ldap == 'shubham' and password == 'bhardwaj':
            return render(request, 'login/home.html', {'form' : form})
        else:
            form = LoginForm()
            return render(request, 'login/home.html', {'form' : form})


'''Check if details are correct, then redirect to student/faculty
return redirect(student:home)
print({'ldap','password'})'''



