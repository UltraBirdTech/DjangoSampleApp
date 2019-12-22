from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendSearchForm
from .forms import FriendFindForm
from .forms import FriendForm
from django.db.models import Q

def index(request):
    params = {
        'title': 'Hello',
        'message': 'all firends.',
        'search_form': FriendFindForm,
        'data': [],
    }
    if (request.method == 'POST'):
        string = request.POST['find']
        form = FriendFindForm(request.POST)
        params['data'] = Friend.objects.filter(Q(name__contains=string)|\
            Q(id__contains=string) |\
            Q(mail__contains=string))
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
     }
    return render(request, 'hello/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = 'search result'
        form = FriendFindForm(request.POST)
        string = request.POST['find']
        data = Friend.objects.filter(Q(name__contains=string)|\
            Q(id__contains=string) |\
            Q(mail__contains=string))
    else:
        msg = 'search words...'
        form = FriendFindForm(request.POST)
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)
