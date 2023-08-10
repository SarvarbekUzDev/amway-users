from django.db import models

from apps.users.models import Users

# Create your models here.
class Workers(models.Model):
	worker_id = models.IntegerField()
	name = models.CharField(max_length=20)
	mail = models.EmailField(max_length=50)

	def __str__(self):
		return self.mail


class Products(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	number = models.PositiveIntegerField()
	price = models.FloatField()
	daily_amount = models.PositiveIntegerField(blank=True, null=True)
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=True)

	worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
	user = models.ForeignKey(Users, on_delete=models.CASCADE)

	def __str__(self):
		return self.name