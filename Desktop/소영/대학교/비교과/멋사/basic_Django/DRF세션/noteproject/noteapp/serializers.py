from rest_framework import serializers
from .models import Note

class SimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('title','created')

class DetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('title', 'description', 'created')

class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('title', 'description')