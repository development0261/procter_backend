from django.contrib import admin
from Placement_site.models import *

from django.contrib.auth.models import Group

admin.site.unregister(Group)
# # Register your models here.


class Interview_Language_data(admin.ModelAdmin):
            
    def make_active(modeladmin, request, queryset):
        queryset.update(isactive='active')
    make_active.short_description = "Active Selected Language"
    
    def make_inactive(modeladmin, request, queryset):
        queryset.update(isactive='inactive')
    make_inactive.short_description = "Inactive Selected Language"
    
    list_display=('language','isactive')
    # list_filter = ['subject','created_at','isactive']
    list_per_page = 10
    list_display_links=("language",)
    ordering=('created_at','updated_at','isactive')

    actions = [make_active,make_inactive]
admin.site.register(Interview_Language,Interview_Language_data)

class Language_Settings_data(admin.ModelAdmin):
            
    def make_active(modeladmin, request, queryset):
        queryset.update(isactive='active')
    make_active.short_description = "Active Selected Exam Details"
    
    def make_inactive(modeladmin, request, queryset):
        queryset.update(isactive='inactive')
    make_inactive.short_description = "Inactive Selected Exam Details"
    
    list_display=('interview_language_id','beginner_level','beginner_level_hours','intermediate_level',
                  'intermediate_level_hours','advanced_level','advanced_level_hours',
                  'isactive')
    # list_filter = ['subject_id','created_at','updated_at']
    list_per_page = 10
    list_display_links=("interview_language_id",)
    ordering=('created_at','updated_at')

    actions = [make_active,make_inactive]
admin.site.register(Language_Settings,Language_Settings_data)

class Exam_Instruction(admin.ModelAdmin):
            
    def make_active(modeladmin, request, queryset):
        queryset.update(isactive='active')
    make_active.short_description = "Active Selected Exam Details"
    
    def make_inactive(modeladmin, request, queryset):
        queryset.update(isactive='inactive')
    make_inactive.short_description = "Inactive Selected Exam Details"
    
    list_display=('instruction_id','instruction','isactive')
    # list_filter = ['isactive','created_at','updated_at']
    list_per_page = 10
    list_display_links=("instruction_id","instruction",)
    ordering=('created_at','updated_at')

    actions = [make_active,make_inactive]
admin.site.register(ExamInstructions,Exam_Instruction)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
class User_settings_data(BaseUserAdmin):
               
    list_display=('username','password','email')
    list_display_links=(["username"])
    list_per_page = 10
    ordering=(['username'])

    fieldsets = (
        ('User Credentials', {'fields': ('username','email', 'password')}),
    )
    
admin.site.register(User_settings,User_settings_data)
# ----------------------------------------------------------------
admin.site.site_header = "Logix Built Infotech Admin"
admin.site.site_title = "Logix Built Infotech Admin Portal"
# admin.site.index_title = "Admin Portal"
admin.site.site_url=''

