from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import SignupForm

def logout_view(request):
    logout(request)
    return redirect('core:home')

def signup(request):
    if request.method=='POST':
        signupForm=SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            return redirect('login:login')
       
    else:
        signupForm=SignupForm()
    return render(request,'login/signup.html',{'signupForm':signupForm})