from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def registration(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    return render(request, 'register.html')