from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response



class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'
		# fields = ('customer', 'product', 'datetime')


@api_view(['GET', 'POST'])
def user_list(request):
	"""
	List all user, or create a new one
	"""
	if request.method == 'GET':
		customers = Customer.objects.all()
		serializer = CustomerSerializer(customers, many = True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		try:
			username = request.data['username']
			pwd = request.data['pwd']
			user = User.objects.create_user(username, email=None, password = pwd)
			user.save()
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)

		u = User.objects.get(username = username)
		data = {"user": u.pk, "first_name": request.data['first_name'], "last_initial": request.data['last_initial']}
		serializer = CustomerSerializer(data = data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	

@api_view(['GET', 'DELETE'])
def user_detail(request, pk):
	"""
	Retrieve or delete a user instance
	"""
	try:
		customer = Customer.objects.get(pk=pk)
	except Customer.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		u = customer.user
		print u.pk
		serializer = CustomerSerializer(customer)
		return Response(serializer.data)

	elif request.method == 'DELETE':
		u = customer.user
		customer.delete()
		u.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def order_list(request):
	"""
	List all orders, or create a new one
	"""
	if request.method == 'GET':
		orders = Order.objects.all()
		serializer = OrderSerializer(orders, many = True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		user_id = request.data['user']
		customer = Customer.objects.get(user=user_id)
		data = {"customer": customer.pk, "product": request.data['product']}
		serializer = OrderSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
@api_view(['GET', 'DELETE'])
def order_detail(request, pk):
	"""
	Retrieve or delete a order instance
	"""
	try:
		order = Order.objects.get(pk=pk)
	except Order.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ProductSerializer(order)
		return Response(serializer.data)

	elif request.method == 'DELETE':
		order.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)