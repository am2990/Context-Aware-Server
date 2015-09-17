from django.db import models

# Create your models here.

class Sensor(models.Model):
	name = models.CharField(max_length=120, blank=False)
	value = models.DecimalField(blank = False, max_digits=5, decimal_places = 2)
	timestamp = models.DateTimeField(max_length=50, blank=False)

class User(models.Model):
	"""docstring for ClassName"""
	uid = models.CharField(max_length=50, blank=False, primary_key=True)
	name = models.CharField(max_length=120, blank=False)
	activity = models.CharField(max_length=50, blank=False)
	sensors  = models.ManyToManyField(Sensor, related_name = "userforsensor")
	timestamp = models.DateTimeField(max_length=50, blank=False)
