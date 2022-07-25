from rest_framework import serializers
from .models import Note

class SimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('id','type','text','like')

class DetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('id','type','text','like')

class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('type', 'text')