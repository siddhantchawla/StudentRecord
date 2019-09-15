from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
import pyqrcode
import qrtools
import random
import string
from .scanner import *
from authentication.models import *
from .models import *
# Create your views here.

def test(request):
	if request.user.is_superuser == True:
		return True
	return False

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@login_required(login_url = '/auth/login')
def index(request):
	user = Userprofile.objects.filter(user = request.user).first()
	print(user)
	request.session['hash'] = randomString(10)
	print("hash    "+request.session['hash'])
	text = request.session['hash']+str(user.regNum)
	response = {}
	response["contact"] = text
	return render(request,'record/home.html',response)

def scan(request):
	#assuming i get the image
	qr = scanned()
	data = qr.decode("utf-8")
	s = data[:10]
	reg = data[10:]
	print("hash    "+request.session['hash'])
	if s==request.session['hash']:
		obj = Record.objects.filter(regNum = reg,status = 1).first()
		if obj:
			obj.status = 0
			obj.save()
		else:
			ob = Record(regNum = reg,status = 1)
			ob.save()
	# request.session['hash'] = randomString(10)
	return redirect('/scan')
	

@user_passes_test(test)
@login_required(login_url = '/auth/login')
def list(request):
	rec = Record.objects.filter(status = 1).order_by('-date')
	data = {}
	data['student'] = []
	for l in rec:
		d = {}
		user = Userprofile.objects.filter(regNum = l.regNum).first()
		u = User.objects.filter(user = user).first
		d['name'] = u.first_name + " " + u.last_name
		d['contact'] = l.contact
		d['regNum'] = l.regNum
		d['date'] = l.date
		data['student'].append(d)

	return render(request,'record/list.html',data)





	