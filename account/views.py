from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'home.html', {'is_homepage': True})

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')


def signuppage(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        unm = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        
        try:
            user=User.objects.get(username=unm,password=pwd)
            return render(request,'signin.html')
        
        except:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=unm,email=email,password=pwd)
            user.save()
            return render(request,'signin.html')
    else:
        return render(request,'signup.html')
    
def signinpage(request):
    if request.method=="POST":
        unm=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=unm,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('userhome')
        
        else:
            return render(request,'signin.html')
        
def userhome(request):
    return render(request,'userhome.html')

def edit_profile(request):
    # Placeholder view for editing user profile
    return render(request, 'edit_profile.html')
    
def logout(request):
    auth.logout(request)
    return render(request,'signup.html')

def view_team(request):
    # Placeholder view for viewing team directory
    return render(request, 'view_team.html')

def my_profile(request):
    # View for displaying user profile
    return render(request, 'my_profile.html')

