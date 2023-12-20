from student.models import *
from datetime import datetime
# exec(open(r'D:\Sheetal\Python\Scripting files\Django_Projects\StudentProject\student\db_shell.py').read())


# active_stu = Student.objects.filter(is_active = True)
# print(active_stu)

'''Custom module manager'''
# active_stu = Student.objects.get_active_stud_objects()
# print(active_stu)

'''Multiple database'''
# 1. database.config, mention credentials for different databases
# 2. create database in backend with name of second database
# 3. in settings.py, add one more key value pair in DATABASES
# 4. now we dont have any tables in second database, for creating those we have to migrate the tables
'''5. . #command -  python manage.py migrate --database=second'''  #(where second is the key name of second database from settings.py)
# 6. Now for further orm queries we should mention in the command itself that we are using diffrent database

###this normal comand by default create object in 'default' database
# Student.objects.create(first_name = "stud10", last_name = "las10", 
#                                    date_of_birth = datetime(22, 10, 3),
#                                    address = "pune", phone_number = 2334234, 
#                                    department_name = "computer", gender = "M")

####When we want to use different database
# Student.objects.using("second").create(first_name = "stud10", last_name = "las10", 
#                                    date_of_birth = datetime(22, 10, 3),
#                                    address = "pune", phone_number = 2334234, 
#                                    department_name = "computer", gender = "M")
