from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(Q(username  = username) | Q(email = email))
        if user_obj.exists():
            messages.error(request , "Username or email already exist!")
            redirect('/profile/register')
        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
        )
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request , "Your account has been created!")
        redirect('/login')
        
        
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username)
        if not user_obj.exists():
            messages.error(request , "Account does't exist")
            return redirect('/login/')
        user_obj = authenticate(username = username, password = password)
        if not user_obj:
            messages.error(request, "Invalid Credential")
            return redirect('/login/')

        login(request,user_obj)
        return redirect('/')
        
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    messages.success(request, "logout successful")
    return redirect('/login')