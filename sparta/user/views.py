from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib import auth

# Create your views here.


def signup(request):
    if request.method == "GET":
        return render(request, 'user/signup.html')

    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        UserModel.objects.create_user(
            username = username, 
            password = password,
            phone = phone,
            address = address
        )

        return redirect('user:login')


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

      

        username = UserModel.objects.get(username = username)
        print(username)
        user = auth.authenticate(request, username = username, password = password)
        print(user)
        
        if user is not None:
            auth.login(request,user)
            return render(request, 'home.html')
        else:
            return redirect('user:login')

    