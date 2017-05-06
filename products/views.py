# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def home(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products': products,})

def admin(request):
	products = Product.objects.all()
	return render(request, 'admin-products.html', {'products': products,})
