
from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("student_details/<str:enrollment_no>",views.student_details),
    path("exam_details/<str:subject_id>/<str:student_id>",views.exam_details),
    path("subject_details/",views.subject_details),
    path("student_login/<str:enroll>/<str:passwd>",views.student_login),
    # path("student_login/",views.student_login),
    path("get_exam_hours/<str:subject>",views.get_exam_hours),
    path("exam_instruction/",views.exam_instruction),
]
