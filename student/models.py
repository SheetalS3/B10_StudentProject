from django.db import models

# Create your models here.

class CustomStudentManager(models.Manager):             #Custom manager 1
    def get_active_stud_objects(self):
        return self.filter(is_active = False)
    
    def get_inactive_stud_objects(self):
        return self.filter(is_active = True)



class Student(models.Model):
    DEPARTMENTS = [
        ('comp', 'Computer'),
        ('mech', 'Mechanical'),
        ('et', 'E&T'),
    ]

    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    is_active = models.BooleanField(default= False)
    department_name = models.CharField(max_length=20, choices= DEPARTMENTS, null= True)
    gender = models.CharField(max_length=5, choices=GENDER, null=True)
    objects = CustomStudentManager()                                       #Custom manager 2 
                                                                           #Query - active_stu = Student.objects.get_active_stud_objects()
                                                                                    # print(active_stu)

    def __str__(self):
        return self.first_name
    
'''------------------------------------Uploading a File------------------------------------------'''    

class UploadFile(models.Model): # uploaded file will not be stored in database directly. File will be stored in uploads folder. 
    file_name = models.CharField(max_length=50)     # It just saves the file path of uploads in the database. 
    upload_file = models.FileField(upload_to='uploads/')    #upload_to: specifies the directory where the files will be stored.
    # uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.file_name}"
    
    class Meta:
        db_table = "file_upload"





                         

















