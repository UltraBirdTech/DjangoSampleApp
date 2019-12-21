from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    params = {
        'title': 'Hello/Index',
        'msg': 'This is a sample message',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'Hello/Next',
        'msg': 'This is a other sample page.',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)
