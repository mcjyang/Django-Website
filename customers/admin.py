# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.

class CustomerInline(admin.StackedInline):
	model = Customer
	can_delete = False
	verbose_name_plural = 'customer'

class UserAdmin(BaseUserAdmin):
	inlines = (CustomerInline,)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('user', 'first_name', 'last_initial')

class OrderAdmin(admin.ModelAdmin):
	list_display = ('customer', 'product', 'datetime')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)