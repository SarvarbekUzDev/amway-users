from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Products
from apps.products.serializers import ProductSerializer


# Create your views here.
@api_view(['GET'])
def UserProductsView(request, user_id, worker_id):
	products = Products.objects.filter(
		user_id=user_id, 
		worker__worker_id=worker_id
	)
	print(products, " OK")
	serializer = ProductSerializer(products, many=True)

	return Response(serializer.data)
