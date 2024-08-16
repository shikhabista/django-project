from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.Forms.StudentForm import StudentForm
from app.models import student


# Create your views here.

def home(request):
    return HttpResponse("Welcome to home page")


def about(request):
    return HttpResponse("Welcome to about page")


def read(request):
    students = student.objects.all()
    return render(request, 'read.html', {'students': students})


def delete(request, id):
    std = student.objects.get(id=id)
    std.delete()
    return redirect('/read/')


def create(request):
    form = StudentForm
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/read/')
    return render(request, 'create.html', {'form': form})


@login_required(login_url='/login/')
def update(request, id):
    studentt = student.objects.get(id=id)
    print(studentt)
    form = StudentForm(instance=studentt)
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        if (form.is_valid):
            form.save()
            return redirect('/read/')
    return render(request, 'create.html', {'form': form})


def loginn(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            return redirect('/read/')
        return render(request, 'login.html')


def logoutt(request):
    logoutt(request)
    return redirect('/login/')


def registerr(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username=username, password=password, email=email)
        return redirect('/login/')
    return render(request, 'register.html')
