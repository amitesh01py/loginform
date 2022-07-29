from ast import Try
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        # to create a user
        if request.POST['password'] == request.POST['passwordagain']:
            # both the password matched
            # now check if previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {"error":"username already exist"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                # this ine can login user right now
                auth.login(request, user)
                return redirect(home)
        else:        
            return render(request, 'register.html', {"error":"Password Don't Match"})
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        # check if a user is exists
        # with username and password then
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'showme.html')
        else:
            return render(request, 'home.html', {"error":"invalid login credentials"})
    return render(request, 'home.html')   

def logout(request):
    auth.logout(request)
    return redirect(home)         