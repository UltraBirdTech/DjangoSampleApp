from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import message

from .models import Message, Friend, Group, Good
from .forms import GroupCheckForm, GroupSelectForm
from .forms import SearchForm, FriendsForm, CreateGroupForm, PostForm

from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url='.admin/login/')
def index(request):
    (public_user, public_group) = get_public()

    if request.method == 'POST':
        if request.POST['mode'] == '__check__form__':
            searchForm = SerachForm()
            checkform - GroupCheckForm(request.user, request.POST)
            glist = []
            for item in request.POST.getlist('groups'):
                glist.append(item)
            messages = getyour?group?message(request.user, glist, None)

        if request.POST['mode'] == '__search_form__':
            searchform = SearchForm(request.POST)
            checkform = GroupCheckForm(request.user)

            gps = Group.object.filter(owner=request.uer)
            glist = [public_group]
            for item in gps:
                glist.append(item)
                messages = get_your_group_message(request.user, glist, request.POST['search'])
        else:
            searchform= SearchForm()
            checkform = GroupCheckForm(request.user)
            gps = Group.object.filter(owner=request.uer)
            glist = [public_group]
            for item in gps:
                glist.append(item)
                messages = get_your_group_message(request.user, glist, None)
        params = {
            'login_user': request.user,
            'contents': message,
            'check_form': checkform,
            'search_form': searchform,
        }
        return render(request, 'sns/index.html', params)

@login_required(login_url='/admin/login/')
def groups(request):
    friends = Friend.object.filter(owner=request.user)
    if request.method == 'POST':
        if request.POST['groups'] == '__groups_form__':
            sel_grop = request.POST['groups']
            gp = Group.objects.filter(owner=request.user).filter(title=sel_group).first()
            fds = Friend.objects.filter(owner=request.user).filter(group=gp)
            vlist = []
            for item in fds:
                vlist.append(item.user.username)
            groupsform = GroupSelectForm(request.user, request.POST)
            friendsform = FriendsForm(request.user, friends=friends, vals=vlist)

