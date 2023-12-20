from django.shortcuts import render, HttpResponse, redirect
from .models import Student, UploadFile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def welcome(request):
    all_Stu_db = Student.objects.all()
    return render (request, "home.html", {"all_Stu_db" : all_Stu_db})
 
def student_registration(request):
    all_stu = Student.objects.all()
    departments_db = Student.DEPARTMENTS
    if request.method =='GET':
        return render(request, "addStudent.html", {"departments_db" : departments_db, 'all_stu': all_stu})
    elif request.method == 'POST':
        data = request.POST
        if not data.get("id_html"): # Jeva add click hoil teva html page varcha id_html nasnare, so to data save hoil mhanje backend madhe
                                    # new student object create hoil
            Student.objects.create(first_name = data.get('firstName_html'), last_name = data.get('last_name_html'), 
                                   date_of_birth = data.get('date_of_birth_html'),
                                   address = data.get('address_html'), phone_number = data.get('phone_number_html'), 
                                   department_name = data.get('department_html'), gender = data.get('gender_html'))
        else:
            s_obj = Student.objects.get(id = int(data.get("id_html"))) # id la match honara stu record fetch zala in s_obj
            s_obj.first_name = data.get("firstName_html")   
            s_obj.last_name = data.get("last_name_html")
            s_obj.date_of_birth = data.get("date_of_birth_html")
            s_obj.address = data.get("address_html")
            s_obj.phone_number = data.get("phone_number_html")
            s_obj.department_name = data.get("department_html")
            s_obj.gender = gender = data.get('gender_html')
            s_obj.save()            #4. ata jeva update click hoil (addstu.html page var asalela update button) teva html page varcha id_html yeil,
                                    #5.tya id la match honar record fetch hoil in s_obj. so to s.obj use karun , html kadun yenarya values (name field use karun ikade anaychya)
                                    # ani update karaychya

        return redirect("homepage")
    
def edit_stud_info(request, stID_frm_front):                #1.Homepage varchya update button click kelyavar he function invoke to ek id gheun ala
    departments_db = Student.DEPARTMENTS                    #2.tya id related records fetch karun render kele add.html var thru specific_stu_obj
    try:                                                    #3.mag html page var specific_stu_obj yatun id kadhala, name kadhala {{in values field madhe}}...
        stu_obj = Student.objects.get(id = stID_frm_front)    #get record of student whose id is equal to id coming from html front end
    except Student.DoesNotExist:
        return HttpResponse("Student record is not present")
    else:
        return render(request, "addStudent.html", {"specific_stu_obj": stu_obj, "departments_db" : departments_db}) 
                                                        # ata hi key zali tya particular student chi...ti use karaychi
                                                                                 # to show this data on front end
    
        
# <!-- 1.After clicking on add, POST request janar..ani ha form return honar display honar  -->
# <!-- 1.After clicking on submit, backend la NAME field gheun janar  -->

# <!-- 2.After click on update, POST request janar ani ha 'id_html' gheun janar -->
# <!-- Ata backend kadun data yenar to VALUE madhe specify kela in {{}} ki to html page var display honar -->

def delete_stud_info(request, stID_frm_front):
    try:
        stu_obj = Student.objects.get(id = stID_frm_front)
    except Student.DoesNotExist:
        return HttpResponse("Student record is not present")
    else:
        if request.POST.get("hard_delete")== "hard_del":
            stu_obj.delete()
        else:
            stu_obj.is_active = True
            stu_obj.save()
        return redirect("homepage")
    
def show_deleted_stud(request):
    deleted_studs_obj = Student.objects.filter(is_active = True)
    return render(request, "deletedStudent.html", {"deleted_studs_obj": deleted_studs_obj})

def restore_student(request, stID_frm_front):
    restore_stud = Student.objects.get(id = stID_frm_front)
    restore_stud.is_active = False
    restore_stud.save()
    return redirect("homepage")
    


'''When to use which return'''
 
# html - return render(request, "addStudent.html")
# httprequest response - return HttpResponse("Book saved succesfully..")
# dusrya page var redirect...redirect import karava lagato - return redirect("home")		jeva kuthe redirect vhaycha nasat fakt backend la
#                                                                                            change keleli ek single 
# 																						value front end la display karaychi asate

'''----------------------------------------Forms---------------------------------------------------------'''

from .forms import My_form, FileUploadForm

def my_form_view(request):
    form_obj = My_form()
    return render(request, 'my_django_form.html', {'my_form_obj': form_obj})


'''-----------------------------------File upload------------------------------------'''

def UploadFileView(request):
    if request.method == 'POST':
        file_obj = FileUploadForm(request.POST, request.FILES) # request will bring all data from front end that is whatever we enter 
        if file_obj.is_valid():                                 # in the fields and filepath in FILES
            file_obj.save()
            return redirect('file-list')
    else:
        file_obj = FileUploadForm()
    return render(request, 'uploadFile_form.html', {"file_obj": file_obj})

def listOf_Uploaded_Files(request):
    all_uploded_files = UploadFile.objects.all()
    return render(request, 'show_uploaded_files.html', {'all_uploded_files': all_uploded_files})
  












