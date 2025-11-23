from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_(request):
    if request.method == 'POST':
        user = request.POST['username']
        pasw = request.POST['password']
        print(user,pasw)
        a = authenticate(username=user,password=pasw)
        
        if a:
            login(request,a)
            return redirect('home')
        else:
            return render(request,'login_.html',{'status':True})
    return render(request,'login_.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            a = User.objects.get(username=username)
            return render(request,'register.html',{'status':True})
    
        except:
            a = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username
            )
        a.set_password(password)
        a.save()
        return redirect('login_')
        
    return render(request,'register.html',{'status':False})

def logout_(request):
    logout(request)
    return redirect('login_')


@login_required(login_url="login_")
def profile(request):
    return render(request,'profile.html')

def reset(request):
    if request.method == "POST":
        u = User.objects.get(username=request.user)
        old_pasw = request.POST['oldpasw']
        u = authenticate(username=u.username,password=old_pasw)
        
        if u:
            new_pasw = request.POST['newpasw']
            u.set_password(new_pasw)
            u.save()
            return render(request,'reset.html',{'status':True})
        else:
            return render(request,'reset.html',{'old_pasw':True})
    return render(request,'reset.html')