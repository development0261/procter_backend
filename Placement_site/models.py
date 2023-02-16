
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

 # Create your models here.
    
    
class User_settings(AbstractUser):
    username = models.CharField(max_length=20,unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True,max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True,default=datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True) 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password','email']   
    class Meta:
        verbose_name = "User Settings"
        verbose_name_plural = "User Settings"
 
class Interview_Language(models.Model)  :
    
    interview_language_id = models.AutoField(primary_key=True, auto_created=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    isactive=models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.language}"

    class Meta:
        verbose_name = "Interview Language"
        verbose_name_plural = "Interview Language"
        
class Language_Settings(models.Model):
    
    Language_Settings_id= models.AutoField(primary_key=True, auto_created=True)
    interview_language_id=models.ForeignKey(Interview_Language,on_delete=models.CASCADE)
    beginner_level=models.URLField(max_length = 200,null=True,blank=True)
    beginner_level_hours=models.TimeField(max_length=10,null=True,blank=True,default=datetime.now())
    intermediate_level=models.URLField(max_length = 200,null=True,blank=True)
    intermediate_level_hours=models.TimeField(max_length=10,null=True,blank=True,default=datetime.now())
    advanced_level=models.URLField(max_length = 200,null=True,blank=True,)  
    advanced_level_hours=models.TimeField(max_length=10,null=True,blank=True,default=datetime.now())
    isactive=models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.Language_Settings_id}"

    class Meta:
        verbose_name = "Language Settings"
        verbose_name_plural = "Language Settings"
        
class ExamInstructions(models.Model):
    instruction_id=models.AutoField(primary_key=True, auto_created=True)
    instruction=models.CharField(max_length=2024, null=False, blank=True)
    isactive=models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    
    class Meta:
        verbose_name = "Exam Instructions"
        verbose_name_plural = "Exam Instructions"
     
    