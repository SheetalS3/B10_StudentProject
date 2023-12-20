from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

'''------Create user registration form--------'''

class NewUserForm(UserCreationForm):            # user creation cha built in form ahe to apan ithe inherite karat ahot. Tyat built in fields ahet
	email = forms.EmailField(required=True) # user name, pwd1, pwd2...We are adding new field that is email

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2") # these fields we will see on our form

	def save(self, commit=True):                # save method is there in usercreation form already, we are overriding that and additionally we are asking to save email field
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user