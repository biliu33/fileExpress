# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'index.html', {'errorMessage': ''})


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == 'admin' and password == '123':
            return HttpResponseRedirect('/login/event_manage/')
        else:
            return render(request, 'index.html', {'errorMessage': 'username or password error'})


def event_manage(request):

    return render(request, "event_manage.html")
