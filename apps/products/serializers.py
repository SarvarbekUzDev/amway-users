from collections import OrderedDict
from rest_framework import serializers

from .models import Workers, Products
 

class WorkersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workers
		fields = ('id','worker_id','name','mail',)



class ProductSerializer(serializers.ModelSerializer):
	worker = WorkersSerializer()

	class Meta:
		model = Products
		fields = ('id','name','description','price',
							'number','daily_amount','user','worker','date','active')

		read_only_fileds = ('id',)

	def to_representation(self, instance):
		data = super().to_representation(instance)
		if data['active']:
			return data

		return OrderedDict()

	def update(self, instance, validated_data):
		print(instance, validated_data, " :)))")
		instance.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.price = validated_data.get('price', instance.price)
		instance.daily_amount = validated_data.get('daily_amount', instance.daily_amount)
		instance.number = validated_data.get('number', instance.number)
		instance.user = validated_data.get('user', instance.user)
		worker_data = validated_data.get('worker')
		if worker_data:
			worker_serializer = WorkersSerializer(instance.worker, data=worker_data)
			worker_serializer.is_valid(raise_exception=True)
			worker_serializer.save()
			instance.worker.id = worker_serializer.data.get("id")

		instance.save()
		return instance

	def create(self, validated_data):
		name = validated_data.get("name")
		description = validated_data.get("description")
		price = validated_data.get("price")
		daily_amount = validated_data.get("daily_amount")
		number = validated_data.get("number")
		user = validated_data.get("user")
		worker = validated_data.get("worker")

		try:
			worker = Workers.objects.create(
				worker_id=worker['worker_id'],
				name=worker['name'],
				mail=worker['mail']
			)
			create_product = Products.objects.create(
				name=name,
				description=description,
				price=price,
				daily_amount=daily_amount,
				number=number,
				user=user,
				worker=worker
			)

			return create_product
		except Exception as e:
			raise serializers.ValidationError(f"{e}")