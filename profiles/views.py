from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def profile(request):
    return render(request, 'profile.html')

