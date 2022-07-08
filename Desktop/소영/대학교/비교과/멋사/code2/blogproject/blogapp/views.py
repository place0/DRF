import imp
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, Comment, CommentForm
def home(request):
	#블로그 글들 모두 다 띄우는 코드
	#posts = Blog.objects.all()
	posts = Blog.objects.filter().order_by('-date')
	return render(request, 'index.html', {'posts':posts})
#블로그 글 작성 html을 보여주는 함수
def new(request):
	return render(request, 'new.html')

#블로그 글 저장해주는 함수
def create(request):
	if(request.method == 'POST'):
		post = Blog()
		post.title = request.POST['title']
		post.body = request.POST['body']
		post.date = timezone.now()
		post.save()
	return redirect('home')

#django의 form을 이용해 입력값을 받고 get,post요청 둘 다 처리 가능
def formcreate(request):
	if request.method =='POST' or request.method == 'FILES':
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			post = 	Blog()
			post.title = form.cleaned_data['title']
			post.body = form.cleaned_data['body']
			post.save()
		return redirect('home')
	else:
		form = BlogForm()
	return render(request, 'form_create.html',{'form':form})


def modelformcreate(request):
	if request.method =='POST':
			form = BlogModelForm(request.POST)
			if form.is_valid():
				form.save()
			return redirect('home')
	else:
		form = BlogModelForm()
	return render(request, 'form_create.html',{'form':form})

def detail(request, blog_id):
	#blog_id번째 블로그 글을 DB로 부터 가져와 detail.html로 띄우는 코드
	blog_detail= get_object_or_404(Blog, pk=blog_id)
	
	comment_form = CommentForm()


	return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})


def create_comment(request, blog_id):
	filled_form = CommentForm(request.POST)

	if filled_form.is_valid():
		finished_form = filled_form.save(commit=False)
		finished_form.post = get_object_or_404(Blog, pk=blog_id)
		finished_form.save()

	return redirect('detail', blog_id)


