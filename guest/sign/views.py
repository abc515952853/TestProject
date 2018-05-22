# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username=='admin'and password =='admin123':
            response=HttpResponseRedirect('/event_manage/')
            request.session['user']=password
            return response
        else:
           ##return  HttpResponse('login failed!')
            return render(request,'index.html',{'error':'username or passworderror!'})
def event_manage(request):
    username= request.session.get('user','')
    return render(request,"event_manage.html",{'user':username})