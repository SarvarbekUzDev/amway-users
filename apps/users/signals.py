from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

from .models import Users


@receiver(pre_save, sender=Users)
def SendTokenEmail(sender, instance, **kwargs):
	print(instance, " + ", instance.id)
	# if not instance.id and not instance.is_superuser:
	# 	subject = "Tasdiqlash"
	# 	message = f"""Salom {instance.name}\n\nParol:  {instance.token}"""

	# 	send_mail(
	# 		subject, 
	# 		message, 
	# 		settings.EMAIL_HOST_USER, 
	# 		[instance.mail], 
	# 		fail_silently=False
	# 		# html_message=html_message
	# 	)