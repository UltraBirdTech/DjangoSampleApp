from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendSearchForm
from .forms import FriendCreateForm

def index(request):
    params = {
        'title': 'Hello',
        'message': 'all firends.',
        'search_form': FriendSearchForm,
        'data': [],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = FriendSearchForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendCreateForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendCreateForm(),
    }
    return render(request, 'hello/create.html', params)

