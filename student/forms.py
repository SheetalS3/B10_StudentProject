from django import forms
from .models import UploadFile

'''Django forms'''
class My_form(forms.Form):                  #ha form apan direct banavat ahot, not from module so just forms.Form
    name = forms.CharField(max_length= 100)
    email = forms.EmailField()
    age = forms.IntegerField()


'''File upload'''
class FileUploadForm(forms.ModelForm):      #ha form apan module madhalya fileds pasun banavat ahot so forms.ModelForm
    class Meta:
        model = UploadFile
        fields = ['file_name', 'upload_file']