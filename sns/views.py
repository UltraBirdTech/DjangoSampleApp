from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import message

from .models import Message, Friend, Group, Good
from .forms import GroupCheckForm, GroupSelectForm
from .forms import SearchForm, FriendsForm, CreateGroupForm, PostForm

from django.db.models import Q
from django.contrib.auth.decorators import login_required

