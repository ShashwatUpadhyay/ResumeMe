from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import UserExtra,Expirence
# Create your views here.
@login_required(login_url='/login')
def profile(request):
    user_obj = UserExtra.objects.filter(user = request.user)
    print(user_obj.bio)
    
    if request.method == 'POST':
        profile_photo = request.FILES['profile_photo']
        bio = request.POST.get('bio')
        education = request.POST.get('education')
        skills = request.POST.get('skills')
        city = request.POST.get('city')
        state = request.POST.get('state')
        github = request.POST.get('github')
        linkdin = request.POST.get('linkdin')
        user_obj = UserExtra.objects.update_or_create(
            user = request.user,
            profile_photo = profile_photo,
                            bio = bio,
                            education = education,
                            skills = skills,
                            city = city,
                            state = state,
                            github = github,
                            linkdin = linkdin,)
        return render(request, 'profile.html' ,{'data' : user_obj})
    return render(request, 'profile.html', {'data' : user_obj})

