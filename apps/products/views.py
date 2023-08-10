from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Products


class ProductCreateView(generics.CreateAPIView):
    # permission_classes = []
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
	serializer_class = ProductSerializer

	def put(self, request, product_id):
		product = get_object_or_404(Products, id=product_id)
		serializer = self.serializer_class(product, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)

		return Response(serializer.errors, status=400)


@api_view(['GET'])
def ProductDetailView(self, product_id):
	try:
		product = Products.objects.get(id=product_id)
		serializer = ProductSerializer(product)
		return Response(serializer.data, status=200)
	except Products.DoesNotExist:
		return Response({'error':"Product not found."}, status=404)


@api_view(['DELETE'])
def ProductDeleteView(self, product_id):
	try:
		product = Products.objects.get(id=product_id)
		product.active = False
		product.save()
		return Response({'message':'Product delete.'}, status=200)
	except Products.DoesNotExist:
		return Response({'error':"Product not found."}, status=404)


@api_view(['GET'])
def UserProductsView(self, user_id):
	product = Products.objects.filter(user_id=user_id)
	serializer = ProductSerializer(product, many=True)
	return Response(serializer.data, status=200)
	