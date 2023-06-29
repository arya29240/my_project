from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        use=request.POST['username']
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpass=request.POST['password1']
        if password==cpass:
            if User.objects.filter(username=use).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=use,first_name=fn,last_name=ln,email=email,password=password)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def login(request,):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')