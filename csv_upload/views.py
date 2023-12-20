from django.shortcuts import render, HttpResponse
from .forms import CSVUploadForm
import csv
from .models import Employee

'''------------------------Upload file (the CSV file's data is processed, and instances of a Django model (YourModel) 
are created and saved to the database based on that data. The actual CSV file is not stored in the database.)
So reading the content of the CSV file and saving its data in a structured form, such as in a database or some other data storage.
----------------'''

def handle_upload_csv(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines() #This line reads the content of the CSV file, decodes it as UTF-8, and splits it into lines. This is a common approach to handle CSV files.
    csv_reader = csv.reader(decoded_file)
    headers = next(csv_reader) # yat header la skip kela so that for loop next mhanje 1st row pasun start hoil  # This line uses the next function to retrieve the first row from the CSV file, which is assumed to be the header row. This row contains the names of the columns.
    print("headers----------------------", headers)


    for row in csv_reader:
        employee_data = dict(zip(headers, row))       #zip function 2 list madhun ek ek ele gheun 1:1, 2:2 asa bind karato
        print("row---------------", row)
        Employee.objects.create(**employee_data)         # mhanaje ithe headers madhun ek ani row madhun ek ele yenar ani asa form honar
                                                        # {"first_name": "aa", "last_name": "bb", "email": "aa@gmail.com"}
                                                  
def upload_csv(request):
    if request.method == "POST":
       form = CSVUploadForm(request.POST, request.FILES)       #request post madhe sagala data ani csv file gheun ala from front end
       if form.is_valid():
           handle_upload_csv(request.FILES['csv_file'])          # 'csv_file' comming from forms.py
           return HttpResponse("File uploaded successfully")
    else:
        form = CSVUploadForm()
        return render(request, "upload_csv.html", {"form_v": form})
    


'''-----------------------Download file (means copy file from database and write it in csv form)-------------------'''    

def download_csv(request):
    employees = Employee.objects.all()      #Query the Employee model to get all records

 # Create the HttpResponse object with CSV content
    response = HttpResponse(content_type= 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee_data.csv"'

# Create the CSV writer and write the header
    csv_writer = csv.writer(response)
    csv_writer.writerow(['first_name', 'last_name', 'age'])  # CSV file madhe 1st line header chi write 

# Write data rows
    for employee in employees:
        csv_writer.writerow([employee.first_name, employee.last_name, employee.age])

    return response



    














