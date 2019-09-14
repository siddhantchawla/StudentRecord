from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
import random
import datetime



def login_page(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        try:
            user = User._default_manager.get(username__iexact = user_name.lower())
            username = user.username
        except:
            try:
                user = User.objects.filter(email = user_name).last()
                username = user.username
            except:
                return render(request, 'authentication/login.djt', {'error' : 'User-Name/Password Invalid'})
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user == None :
            return render(request, 'authentication/login.html', {'error' : 'User-Name/Password Invalid'})
        else : 
            login(request,user)
            return redirect('/home')
    return render(request, 'authentication/login.html', None)

def signout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
    	if Userprofile.objects.filter(regNum=request.POST['regNum']).count() > 0:
    		response = {}
    		response['error'] = 'This Registration Number Has Already Been Registered'
    		return render(request, 'authentication/signup.djt', response)
    	username  = request.POST['username']
    	emailadr  = request.POST['email']
    	password  = request.POST['password1']
    	password2 = request.POST['password2']
    	first_name = request.POST['first_name']
    	last_name  = request.POST['last_name']
    	if password != password2 :
    		return render(request, 'authentication/signup.djt', {'error' : 'Passwords don\'t match'})
    	try:
    		user = User._default_manager.get(username__iexact = username.lower())
    		return render(request, 'authentication/signup.djt', {'error':'User-Name Already Exists'})
    	except User.DoesNotExist:
    		user = User.objects.create_user(username = username, email = emailadr, first_name = first_name, last_name = last_name)
    		user.set_password(password)
    		user.save()
    		profile = Userprofile()
    		profile.user = user
    		profile.regNum = request.POST['regNum']
    		profile.branch = request.POST['branch']
    		profile.contact = request.POST['phone']
    		profile.save()
    		user = authenticate(username = username, password = password)
    		login(request, user)
    		return redirect('/home')
        # return redirect('/auth/login')
        
    return render(request, 'authentication/signup.djt', None)