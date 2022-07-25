from turtle import done
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Note
from .serializers import CreateSerializer, DetailSerializer, SimpleSerializer

#글 작성 및 수정, 전체 목록보기
class Notes1APIView(APIView):
	def get(self,request):
		notes = Note.objects
		serializer = SimpleSerializer(notes, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self,request):
		serializer = CreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Note1APIView(APIView):
	def get(self, request, pk):
		note = get_object_or_404(Note, id=pk)
		serializer = DetailSerializer(note)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, pk):
		note = get_object_or_404(Note, id=pk)
		serializer = CreateSerializer(note, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		note = get_object_or_404(Note, pk=pk)
		note.delete()
		return Response()

class DoneNotes1APIView(APIView):
	def get(self,request):
		dones = Note.objects
		serializer = SimpleSerializer(dones, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class DoneNote1APIView(APIView):
	def get(self,request, pk):
		done = get_object_or_404(Note, id=pk)
		done.save()
		serializer = DetailSerializer(done)
		return Response(status=status.HTTP_200_OK)

