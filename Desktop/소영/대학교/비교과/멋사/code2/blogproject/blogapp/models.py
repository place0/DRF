from tkinter import CASCADE
from turtle import title
from django.db import models
from django.forms import modelform_factory

class Blog(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	comment = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Blog, on_delete=models.CASCADE)
	#블로그 글이 삭제된다면 댓글도 같이 삭제하는 것

	def __str__(self):
		return self.comment









