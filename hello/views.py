from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import HelloSearchForm
from .forms import HelloCreateForm

def index(request):
    params = {
        'title': 'Hello',
        'message': 'all firends.',
        'search_form': HelloSearchForm,
        'data': [],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloSearchForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)

def create(request):
    params = { 
        'title': 'Hello',
        'form': HelloCreateForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender= 'gender' in request.POST
        age = request.POST['age']
        birth = request.POST['birthday']
        friend = Friend(name=name, mail=mail, gender=gender, age=age, birthday=birth)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)

