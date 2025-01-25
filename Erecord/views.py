from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        em = request.POST['email']
        ps = request.POST['password']
        ec = request.POST['emcode']
        try:
            user = User.objects.create_user(username=fn, email=em, password=ps)
            EmployeeDetail.objects.create(user=user, emcode=ec)
            error = "no"
        except:
            error = "yes"
    return render(request, 'registration.html')


def em_login(request):
    return render(request, 'em_login.html')
