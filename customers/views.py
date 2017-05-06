# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .api import *
from .models import *
from products.views import *
import json

# Create your views here.

def signup(request):
	if request.method == 'POST':
		r = user_list(request)
		if r.status_code == 201:
			return redirect(login)
		else:
			return render(request, 'signup.html',{})
	else:
		return render(request, 'signup.html', {})


def login(request):
	if request.user.is_authenticated():
		return redirect(home)

	username = request.POST.get('username','')
	pwd = request.POST.get('pwd','')

	user = auth.authenticate(username=username, password=pwd)

	if user is not None and user.is_active:
		auth.login(request, user)
		return redirect(home)
	else:
		return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return redirect(home)


def mycart(request, pk):
	orders = Order.objects.filter(customer = pk)
	serializer = OrderSerializer(orders, many = True)
	orders_data = json.loads(JSONRenderer().render(serializer.data))
	return render(request, 'cart-detail.html', {'orders': orders_data})

def admin_users(request):
	customers = Customer.objects.all()
	return render(request, 'admin-users.html',{'customers': customers})


def admin_carts(request):
	orders = Order.objects.all()
	
	serializer = OrderSerializer(orders, many = True)
	oreders_data = json.loads(JSONRenderer().render(serializer.data))

	customers = Customer.objects.all()
	serializer = CustomerSerializer(customers, many = True)
	customers_data = json.loads(JSONRenderer().render(serializer.data))
	
	return render(request, 'admin-carts.html', {'carts': oreders_data, 'customers': customers_data})
