from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'you typed: "' + msg + '".'
    else:
        result = 'please send msg parameter!'
    return HttpResponse(result)
