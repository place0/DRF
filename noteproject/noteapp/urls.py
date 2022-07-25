from django.urls import path
from .views import DoneNote1APIView, DoneNotes1APIView, Note1APIView, Notes1APIView

urlpatterns = [
	path('note1/', Notes1APIView.as_view()),
	path('note1/<int:pk>/', Note1APIView.as_view()),
	path('done1/',DoneNotes1APIView.as_view()),
	path('done1/<int:pk>/', DoneNote1APIView.as_view()),
]