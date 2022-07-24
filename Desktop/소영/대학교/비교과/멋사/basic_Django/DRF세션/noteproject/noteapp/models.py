from email.policy import default
from turtle import title
from django.db import models

class Note(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title