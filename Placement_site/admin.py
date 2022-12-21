from django.contrib import admin
from Placement_site.models import *

from django.contrib.auth.models import Group

admin.site.unregister(Group)
# Register your models here.

class Student_Profile_data(admin.ModelAdmin):
               
    list_display=('student_id','enrollment_No','first_name','last_name','email','created_at','updated_at')
    list_filter = ['created_at','updated_at']
    list_per_page = 10
    ordering=('created_at','updated_at')
admin.site.register(Student_Profile,Student_Profile_data)

class Subject_details_data(admin.ModelAdmin):
            
    def make_active(modeladmin, request, queryset):
        queryset.update(isactive='active')
    make_active.short_description = "Active Selected Subjects"
    
    def make_inactive(modeladmin, request, queryset):
        queryset.update(isactive='inactive')
    make_inactive.short_description = "Inactive Selected Subjects"
    
    list_display=('subject_id','subject','isactive')
    list_filter = ['subject','created_at','isactive']
    list_per_page = 10
    ordering=('created_at','updated_at','isactive')

    actions = [make_active,make_inactive]
admin.site.register(Subject_details,Subject_details_data)


class Exam_data(admin.ModelAdmin):
            
    def make_active(modeladmin, request, queryset):
        queryset.update(isactive='active')
    make_active.short_description = "Active Selected Exam Details"
    
    def make_inactive(modeladmin, request, queryset):
        queryset.update(isactive='inactive')
    make_inactive.short_description = "Inactive Selected Exam Details"
    
    list_display=('exam_id','subject_id','exam_form_beginner','exam_hours_beginner','exam_form_intermediate','exam_hours_intermediate','exam_form_advanced','exam_hours_advanced','isactive','created_at','updated_at')
    list_filter = ['subject_id','created_at','updated_at']
    list_per_page = 10
    ordering=('created_at','updated_at')

    actions = [make_active,make_inactive]
admin.site.register(Exam_details,Exam_data)

