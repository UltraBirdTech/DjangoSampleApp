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
