from django.db import models

# Create your models here.
class Contacts(models.Model):
	name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	email = models.EmailField()