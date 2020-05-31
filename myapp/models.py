from django.db import models
from django.urls import reverse


# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=50)
	mark=models.IntegerField()

	def get_absolute_url(self):
		return reverse('success', args=[self.id])
