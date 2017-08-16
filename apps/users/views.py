# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import User
# Create your views here.

#GET
def index(request):
    users = User.objects.all()
    context = {'users' : users}
    return render(request,'users/index.html', context = context)
def new(request):
    return render(request,'users/new.html')
def edit(request,number):
    request.session["id"] = number
    request.session["id"] = number
    user = User.objects.get(id = number)
    context = {'user' : user}
    return render(request,'users/edit.html',context=context)
def show(request,number):
    if request.method == "POST":
        request.session["id"] = number
        user = User.objects.get(id = number)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        print user.last_name
        print User.objects.get(id = number).last_name
        return redirect(reverse('user_show',args={number}))
    else:
        request.session["id"] = number
        user = User.objects.get(id = number)
        context = {'user' : user}
        return render(request,'users/show.html',context=context)

def destroy(request,number):
    request.session["id"] = number
    User.objects.get(id = number).delete()
    return redirect(reverse('user_index'))

#POST
def create(request):
    if request.method == "POST":
        new = User.objects.create( first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        request.session["id"] = new.id
        return redirect(reverse('user_show',args={request.session["id"]}))
