from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.
class sandbox_user(models.Model):
	user=models.OneToOneField(User)
	email= models.EmailField(unique=True, max_length=100)
	phone=models.CharField(max_length=100, unique=True)
	api_keys=models.CharField(max_length=100, unique=True)
	api_secret=models.CharField(max_length=100, unique=True)
	date=models.DateTimeField(default=datetime.now, blank=False)
	call_back_url=models.URLField(max_length=200, blank=True)
	confirmation_code=models.CharField(max_length=100,blank=False)
	account_status=models.CharField(max_length=100, default='inactive')

	def __str__(self):
		return self.first_name
	class Meta:
		ordering=['date']
		verbose_name='sandbox_user'
		verbose_name_plural="sandbox_users"
