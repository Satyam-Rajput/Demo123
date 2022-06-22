from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, UserManager
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

from .models import * 
# Create your views here.



def index(request):

    return render(request,'app/index.html')

def userLogin(request):
    return render(request,'app/login.html')

def forgot_password(request):

    return render(request,'app/forgot_password.html')

def signup(request):

    return render(request,'app/signup.html')

def aboutus(request):

    return render(request,'app/about-us.html')

def contactus(request):

    return render(request,'app/contact-us.html')

def purchased_books_details(request):

    return render(request,'app/purchased_books.html')
def issued_books_details(request):

    return render(request,'app/issued_books.html')

def book_details(request):

    return render(request,'app/book_details.html')

def books(request):

    return render(request,'app/books.html')
def by_category(request):

    return render(request,'app/category.html')
def by_author(request):

    return render(request,'app/author.html')


def authenticateUser(request):
    username=request.POST.get('email')
    password=request.POST.get('password')
   
    user=authenticate(username=username,password=password)
    
    
    if user is not None:
       
        if user.is_active:
            
            login(request,user)
            
            return HttpResponse(user.id)
    return HttpResponse('Fail')