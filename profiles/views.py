from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import UserExtra,Expirence
# Create your views here.
@login_required(login_url='/login')
def editprofile(request):
    try:
        user_obj = UserExtra.objects.get(user=request.user)
    except UserExtra.DoesNotExist:
        return render(request, 'profile.html', {'error': 'Profile not found'})
    exp_obj = Expirence.objects.filter(user=request.user).order_by('from_date')
    
    if request.method == 'POST':
        profile_photo = request.FILES.get('profile_photo')
        bio = request.POST.get('bio')
        education = request.POST.get('education')
        skills = request.POST.get('skills')
        city = request.POST.get('city')
        state = request.POST.get('state')
        github = request.POST.get('github')
        linkdin = request.POST.get('linkdin')
        
        # experience
        job_type = request.POST.get('job_type')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        job_role = request.POST.get('job_role')
        organization = request.POST.get('organization')
            
        if job_type or from_date or to_date or job_role or organization:
            exp_obj = Expirence.objects.create(job_type=job_type, from_date=from_date, to_date=to_date, job_role=job_role, organization=organization, user=request.user)
        
        exp_obj = Expirence.objects.filter(user=request.user).order_by('from_date')
        
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
        return redirect('/profile/')
    return render(request, 'profile.html',  {'data': user_obj,'exp': exp_obj})

def profile(request):
    try:
        user_obj = UserExtra.objects.get(user=request.user)
    except UserExtra.DoesNotExist:
        return render(request, 'profilepage.html', {'error': 'profilepage not found'})    
    exp_obj = Expirence.objects.filter(user=request.user).order_by('from_date')
    return render(request, 'profilepage.html',{'data': user_obj,'exp': exp_obj})