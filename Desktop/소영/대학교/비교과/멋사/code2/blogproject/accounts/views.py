from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
#장고가 갖고있던 User에 아이디와 비번(유저 객체) 저장함

def login(request):
	#POST 요청은 로그인처리, GET 요청은 login.html을 띄워주기
	if request.method == 'POST':
		userid = request.POST['username']
		pwd = request.POST['password']
		user = auth.authenticate(request, username=userid, password=pwd)
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else :
			return render(request, 'login.html')

	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('home')