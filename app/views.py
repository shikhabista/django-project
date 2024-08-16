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
        if (form.is_valid):
            form.save()
            return redirect('/read/')
    return render(request, 'create.html', {'form': form})


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