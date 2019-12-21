from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data:',
            'form': HelloForm()
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'name: ' + request.POST['name'] + \
            '<br>mail: '+ request.POST['mail'] + \
            '<br>age: '+ request.POST['age']
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
        
def index(request):
    print(request)
    params = {
        'title': 'Hello/Index',
#        'msg': 'What is your name?',
        'goto': 'next',
        'form': HelloForm()
    }
    if (request.method == 'POST'):
        params['message'] = 'name: ' + request.POST['name'] + \
            '<br>mail: '+ request.POST['mail'] + \
            '<br>age: '+ request.POST['age']
        params['form'] = HelloForm(request.POST)

    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'Hello/Next',
#        'msg': 'This is a other sample page.',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)

def form(request):
#    msg = request.POST["msg"]
    params = {
        'title': 'Hello/Form',
#        'msg': 'Hello!!' + msg + '!!!',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)
