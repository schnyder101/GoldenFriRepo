

from django.db import models
from django.utils import timezone

# Create your models here.
class Tester(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=200,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.email

