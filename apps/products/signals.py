from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Products


@receiver(post_save, sender=Products)
def ProductManage(sender, instance, **kwargs):
	if instance.number == 0 and instance.active:
		instance.active = False
		instance.save()