from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserExtra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    education = models.TextField(null=True,blank=True)
    skills = models.TextField(null=True,blank=True)
    experience = models.TextField(null=True,blank=True)
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)
    city =  models.CharField(max_length=30,null=True, blank=True)
    state =  models.CharField(max_length=30,null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
    linkdin = models.CharField(max_length=200, null=True, blank=True) 
    
    def __str__(self):
        return self.user.first_name
    
class Expirence(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    job_type = models.CharField(max_length=50)
    job_role = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.job_type
