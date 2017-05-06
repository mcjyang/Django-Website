# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.



class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default='', related_name = "customer")
	first_name = models.CharField(max_length = 200)
	last_initial = models.CharField(max_length = 1)
	
	def __str__(self):
		return self.first_name

class Order(models.Model):
	customer = models.ForeignKey(Customer, related_name = "order")
	product = models.ForeignKey('products.Product', related_name = "order")
	datetime = models.DateTimeField(auto_now = True)

