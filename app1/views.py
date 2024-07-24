from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.html import strip_tags
import random
import string
# Create your views here.



@login_required(login_url='login')
def HomePage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')  
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        
        recipient_emails = ['', email]
        
       
        for recipient_email in recipient_emails:
            send_mail(
                'contact',  # subject
                message,  # message
                settings.EMAIL_HOST_USER,  
                [recipient_email],  
                fail_silently=False
            )
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')#from input field name
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        
        if(password1!=password2):
            return HttpResponse("ur password was not entered correctly")
        else:
            my_user = User.objects.create_user(uname,email, password1)
            my_user.save()

            return redirect('login')

    return render(request,'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        print(uname,password)
        user = authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password incorrect!!!")
            
    return render(request,'login.html')


def LogOut(request):
    logout(request)
    return redirect('login')

