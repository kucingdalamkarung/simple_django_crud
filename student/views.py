from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Student


def index(request):
    student = Student.objects.all()
    return render(request, 'student/index.html', context={
        'student': student
    })

def create(request):
    return render(request, 'student/create.html')

def detail(request, pk):
    student = Student.objects.filter(pk=pk).get()
    return render(request, 'student/detail.html', context={
        'student': student
    })

def save(request):
    student = Student(name=request.POST['name'], address=request.POST['address'])
    student.save()

    return HttpResponseRedirect(reverse('student:index'))
