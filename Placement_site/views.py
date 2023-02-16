from django.shortcuts import render

from .models import *
from django.http import HttpResponse,JsonResponse

# Create your views here..

def student_details(request,enrollment_no,passwd):
    if(User_settings.objects.filter(username=enrollment_no,).exists()):
        print(User_settings.objects.get(username=enrollment_no))
        return HttpResponse("Hi")
    else:
        return HttpResponse("Hello")

def exam_details(request,subject_id,student_id):
        
    subject=Interview_Language.objects.filter(language=subject_id).first()   
    data=Language_Settings.objects.all().filter(isactive="True",interview_language_id=subject,student_id=student_id)
    res={}
    for i in data:
        # print(i.student_id)
        res['exam_id']=i.exam_id
        res['exam_date']=i.exam_date
    return JsonResponse(res)

def subject_details(request):
    data=Interview_Language.objects.all().filter(isactive="True")
    res={}
    keys=[]
    values=[]
    for i in data:
        keys.append(i.interview_language_id)
        values.append(i.language)
    res=dict(zip(keys,values))
    return JsonResponse(res)
    
def get_exam_hours(request,subject):

    d1=Interview_Language.objects.get(language=subject)
    data=Language_Settings.objects.filter(isactive="True",interview_language_id=d1)
    res={}
    for i in data:
        
        res['exam_id']=i.Language_Settings_id
        res['exam_form_beginner']=i.beginner_level
        res['exam_hours_beginner']=i.beginner_level_hours
        res['exam_form_intermediate']=i.intermediate_level
        res['exam_hours_intermediate']=i.intermediate_level_hours
        res['exam_form_advanced']=i.advanced_level
        res['exam_hours_advanced']=i.advanced_level_hours
    print(res)
    return JsonResponse(res)
    
def student_login(request,enroll,passwd):
    res={}
    
    if User_settings.objects.filter(username=enroll).exists():
            for i in User_settings.objects.filter(username=enroll):
                
                
                # res['student_id']=i.student_id
                # res['name']=i.first_name+" "+i.last_name
                res['email']=i.email
                # res['password']=i.password
                res['enrollment_No']=i.username
                res['message']="Record Found"
                res['status']= 200
    else:
        res['status']= 400
        res['message']="No Record Found"
                
    return JsonResponse(res)

def exam_instruction(request):
    
    data=ExamInstructions.objects.all().filter(isactive="True")
    res={}
    keys=[]
    values=[]
    for i in data:
        keys.append(i.instruction_id)
        values.append(i.instruction)
    res=dict(zip(keys,values))
    
    return JsonResponse(res) 
            
    

