from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from myapp.models import *



def loginPage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(
            
            username=username,
            password=password,   
        )
        if user:
            login(req,user)
            return redirect('homepage')
        
    
    return render(req,"loginPage.html")




def signupPage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        usertype=req.POST.get('usertype')
        
        password=req.POST.get('password')

        user=CustomUser.objects.create_user(
            username=username,
            email=email,
            usertype=usertype,
            
            password=password, 
        )
        return redirect('loginPage')
        
    return render(req,"signupPage.html")




def logoutPage(req):
    
    logout(req)
    
    return redirect("loginPage")


@login_required 

def homepage(req):
    
    return render(req,"homepage.html")





