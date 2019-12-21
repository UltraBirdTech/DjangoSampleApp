from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    params = {
        'title': 'Hello/Index',
        'msg': 'This is a sample message',
    }
    return render(request, 'hello/index.html', params)
