from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse(content='Hello, world')


def profile(request):
    data = {
        'name': 'Иван',
        'email': 'ivan@mail.ru',
        'phone' : 89656423666
    }
    return render(request, "core/profile.html", context=data)


def tasks(request):
    data = {
        'task1': {'name':'помыть посуду', 'complete': False},
        'task2': {'name':'выкинуть мусор', 'complete': True},
        'task3': {'name':'выгулять собаку', 'complete': False},
    }
    return render(request, "core/tasks.html", context=data)
