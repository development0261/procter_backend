from django.shortcuts import render

from .models import *
from django.http import HttpResponse,JsonResponse

# Create your views here..

def student_details(request,enrollment_no,passwd):
    if(Student_Profile.objects.filter(enrollment_No=enrollment_no,).exists()):
        print(Student_Profile.objects.get(enrollment_No=enrollment_no))
        return HttpResponse("Hi")
    else:
        return HttpResponse("Hello")

def exam_details(request,subject_id,student_id):
    
    print("subject_id : ",subject_id)
    
    subject=Subject_details.objects.filter(subject=subject_id).first()
   
    data=Exam_details.objects.all().filter(isactive="True",subject_id=subject,student_id=student_id)
    # print("-*****************--------",data)
    res={}
    for i in data:
        print(i.student_id)
        res['exam_id']=i.exam_id
        res['exam_date']=i.exam_date
    return JsonResponse(res)

def subject_details(request):
    data=Subject_details.objects.all().filter(isactive="True")
    res={}
    keys=[]
    values=[]
    for i in data:
        keys.append(i.subject_id)
        values.append(i.subject)
    res=dict(zip(keys,values))
    return JsonResponse(res)
    
def get_exam_hours(request,subject):
    data=Exam_details.objects.filter(isactive="True",subject_id=subject)
    res={}
    for i in data:
        res['exam_id']=i.exam_id
        # res['subject_id']=i.subject_id
        res['exam_form_beginner']=i.exam_form_beginner
        res['exam_hours_beginner']=i.exam_hours_beginner
        res['exam_form_intermediate']=i.exam_form_intermediate
        res['exam_hours_intermediate']=i.exam_hours_intermediate
        res['exam_form_advanced']=i.exam_form_advanced
        res['exam_hours_advanced']=i.exam_hours_advanced
    # print(res)
    return JsonResponse(res)
    
def student_login(request,enroll,passwd):
    res={}
    
    if Student_Profile.objects.filter(enrollment_No=enroll).exists():
            for i in Student_Profile.objects.filter(enrollment_No=enroll):
                
                
                res['student_id']=i.student_id
                res['name']=i.first_name+" "+i.last_name
                res['email']=i.email
                # res['password']=i.password
                res['enrollment_No']=i.enrollment_No
                res['mobile']=i.mobile
                res['message']="Record Found"
                res['status']= 200
    else:
        res['status']= 400
        res['message']="No Record Found"
                
    return JsonResponse(res)

# def exam_details(request):
#     pass 
            
    

