from .models import *
from rest_framework import serializers, status
# from rest_framework import viewsets
# from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


# class ProductViewSet(viewsets.ModelViewSet):
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer


# router = DefaultRouter()
# router.register(r'product', ProductViewSet)


@api_view(['GET', 'POST'])
def product_list(request):
	"""
	List all prodcut, or create a new one
	"""
	if request.method == 'GET':
		products = Product.objects.all()
		serializer = ProductSerializer(products, many = True)
		return Response(serializer.data)
	

	elif request.method == 'POST':
		serializer = ProductSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	

@api_view(['GET', 'DELETE'])
def product_detail(request, pk):
	"""
	Retrieve or delete a product instance
	"""

	try:
		product = Product.objects.get(pk=pk)
	except Product.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ProductSerializer(product)
		return Response(serializer.data)

	elif request.method == 'DELETE':
		product.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
