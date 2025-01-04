from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import UserExtra,Expirence
# Create your views here.
@login_required(login_url='/login')
def profile(request):
    try:
        user_obj = UserExtra.objects.get(user=request.user)
    except UserExtra.DoesNotExist:
        return render(request, 'profile.html', {'error': 'Profile not found'})
    
    # print(user_obj.profile_photo,
    #     user_obj.bio,
    #     user_obj.education,
    #     user_obj.skills,
    #     user_obj.city,
    #     user_obj.state,
    #     user_obj.github,
    #     user_obj.linkdin,)
    # print(request.user , user_obj)
    if request.method == 'POST':
        profile_photo = request.FILES.get('profile_photo')
        bio = request.POST.get('bio')
        education = request.POST.get('education')
        skills = request.POST.get('skills')
        city = request.POST.get('city')
        state = request.POST.get('state')
        github = request.POST.get('github')
        linkdin = request.POST.get('linkdin')
        
        if profile_photo:
            user_obj.profile_photo = profile_photo
        user_obj.bio = bio
        user_obj.education = education
        user_obj.skills = skills
        user_obj.city = city
        user_obj.state = state
        user_obj.github = github
        user_obj.linkdin = linkdin
        user_obj.save()

        return render(request, 'profile.html' , {'data': user_obj})
    return render(request, 'profile.html',  {'data': user_obj})

