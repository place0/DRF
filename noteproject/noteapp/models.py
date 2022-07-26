from email.policy import default
from turtle import title
from typing import Type
from django.db import models

class Note(models.Model):
	type = models.IntegerField(default=0)
	text = models.TextField(blank=True)
	like = models.IntegerField(default=0)

	def __str__(self):
		return self.text