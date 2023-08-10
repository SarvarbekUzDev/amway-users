from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import Users


class UserCreateView(generics.CreateAPIView):
    # permission_classes = []
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
	serializer_class = UserSerializer

	def put(self, request, user_id):
		user = get_object_or_404(Users, id=user_id)
		serializer = self.serializer_class(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)

		return Response(serializer.errors, status=400)


@api_view(['GET'])
def UserDetailView(self, user_id):
	try:
		user = Users.objects.get(id=user_id)
		serializer = UserSerializer(user)
		return Response(serializer.data, status=200)
	except Users.DoesNotExist:
		return Response({'error':"User not found."}, status=404)