from django.shortcuts import  render, redirect # render will throw a page to client from server, redirect mhanje trasfer to that page
from .forms import NewUserForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate # login ne login hota ani session table madhe entry hote, logout will remove entry from session table
                                                            # authenticate will authenticate ki jyane login kela to ani system madhe jo ahe to are they both same?
from django.contrib import messages



 # when we hit url from browser, get request will come here and view will render one html page that is register.html jat apala 
 # uname,email,pwd1,pwd2 asel, user will fill the form. Jeva submit button click hoil teva post request yenar... ithech yenar 
 
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect("homepage")
	else:									#if request.methods == 'GET'
            form = NewUserForm()			#'''he full form print karat.....so django form apala sagala form create karun deto just aplyla
			# print(form)					# to form ithe register.html var render karaycha ahe'''
            return render (request=request, template_name="register.html", context={"register_form":form})
	
	#login chya post madhe 2 things will come 1username and another password, to username and pass authenticate karun baghaycha. Authenticate 
	#mhanje to uname and pwd database madhe ahe ki nahi te check karata, then login method will make entry in session table tya entry nantar
	# kuthepan on user interface u can access, click. After logout entry remove hote

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user:		#jar user ahe mhanje user not none ahe tar go to login
				login(request, user)
				return redirect("homepage")
	else:			
		form = AuthenticationForm()
		return render(request=request, template_name="login.html", context={"login_form":form})






