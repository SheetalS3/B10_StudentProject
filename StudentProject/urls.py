"""StudentProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from student.views import welcome, student_registration, edit_stud_info, delete_stud_info, show_deleted_stud, restore_student, my_form_view, UploadFileView, listOf_Uploaded_Files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', welcome, name = 'homepage'),  #Name is like a pet name given to this link for usage in backend
    path('add-student/', student_registration, name = 'add_new_stud'),
    path('edit-student/<int:stID_frm_front>/', edit_stud_info, name = 'edit_stud_info'),
    # After click on update, 'id_html' yenar to insert honar <int:stID_frm_front> ithe ...ithun janar edit_stud_info fn kade-->
    path('delete-student/<int:stID_frm_front>/', delete_stud_info, name = 'delete_stud_info'),
    path('deleted-students/', show_deleted_stud, name = 'deleted_studs'),
    path('restore-students/<stID_frm_front>/', restore_student, name = 'restore_student'),

    path('django-form/', my_form_view, name = 'my_form_view'),  # url for Django forms
    path('upload-file/', UploadFileView, name = 'uploadfile'),  # url for file upload form
    path('file-list/', listOf_Uploaded_Files, name = 'file-list'),  # url for file upload form


    path('csv/', include('csv_upload.urls') ) ,     #include all the urls from csv_upload app, too much urls here, so separating urls from apps
                                                # so pratyek app madhe ek own urls.py create karaychi ani tya url folder la ithe include karaych

    path('user/', include('user_app.urls')), # include all the urls from user_app, 

# http://127.0.0.1:8000/csv/upload-csv/

]
