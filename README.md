# DRF

# 1. models.py
```
class Note(models.Model):
	type = models.IntegerField(default=0)
	text = models.TextField(blank=True)
	like = models.IntegerField(default=0)

	def __str__(self):
		return self.description
```
## type, text, like 변수를 지정해서 각각 게시글 종류, 내용, 좋아요 수를 저장


# 2. serializer
```
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
```
## simpleserializer, detailserializer, createserializer 생성    

# 3. views.py
```
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
```    
## 글 작성 및 수정, 삭제. 전체 목록을 보여주는 함수 작성
