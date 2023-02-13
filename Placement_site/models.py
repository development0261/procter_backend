
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser 


# Create your models here.
class Student_Profile(AbstractUser):
    student_id = models.AutoField(primary_key=True, auto_created=True)
    enrollment_No = models.CharField(max_length=20, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True, unique=True,default="example.com")
    mobile = models.CharField(max_length=20, null=True, blank=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(
        max_length=7, choices=GENDER_CHOICES, null=True, blank=True)
    # profile_image = models.ImageField(null=True, blank=True, upload_to='')
   
    dob = models.DateField(null=True, blank=True,default=datetime.now())
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True,default=datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True) 
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','email']   
    # def __str__(self):
    #     return f"{self.enrollment_No} - {self.name}"

    class Meta:
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profile"
 
class Subject_details(models.Model)  :
    subject_id = models.AutoField(primary_key=True, auto_created=True)
    subject = models.CharField(max_length=20, null=True, blank=True)
    # exam_form=models.URLField(max_length = 200)
    # exam_hours=models.TimeField(max_length=10,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    isactive=models.BooleanField()
    
    def __str__(self):
        return f"{self.subject}"

    class Meta:
        verbose_name = "Subject Details"
        verbose_name_plural = "Subject Details"
        
class Exam_details(models.Model):
    
    exam_id= models.AutoField(primary_key=True, auto_created=True)
    # student_id=models.ForeignKey(Student_Profile,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject_details,on_delete=models.CASCADE)
    # ------------0---------
    exam_form_beginner=models.URLField(max_length = 200,null=True,blank=True)
    exam_hours_beginner=models.TimeField(max_length=10,null=True,blank=True,default=datetime.now())
    exam_form_intermediate=models.URLField(max_length = 200,null=True,blank=True)
    exam_hours_intermediate=models.TimeField(max_length=10,null=True,blank=True,default=datetime.now())
    exam_form_advanced=models.URLField(max_length = 200,null=True,blank=True,)  
    exam_hours_advanced=models.TimeField(max_length=10,null=True,blank=True,default=datetime.now())
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    isactive=models.BooleanField()
    
    def __str__(self):
        return f"{self.exam_id}"

    class Meta:
        verbose_name = "Exam Details"
        verbose_name_plural = "Exams Details"
        
class ExamInstructions(models.Model):
    instruction_id=models.AutoField(primary_key=True, auto_created=True)
    instruction=models.CharField(max_length=2024, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    isactive=models.BooleanField()
    
    class Meta:
        verbose_name = "Exam Instructions"
        verbose_name_plural = "Exam Instructions"
     
    