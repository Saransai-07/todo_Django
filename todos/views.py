from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Task



def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')