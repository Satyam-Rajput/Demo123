
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
      
        path('login/',views.userLogin,name='login'),
        path('authenticate/',views.authenticateUser,name='authenticate'),
        path('',views.index,name='home'),
        path('forgot_password/',views.forgot_password,name='forgot-password'),
        path('signup/',views.signup, name='sign-up'),
        path('aboutus/',views.aboutus, name='about-us'),
        path('contactus/',views.contactus, name='contact-us'),
        path('purchased-books/',views.purchased_books_details, name='purchased-books'),
        path('issued-books/',views.issued_books_details, name='issued-books'),
        path('book-details/',views.book_details, name='book-details'),
        path('books/',views.books, name='books'),
        path('category/',views.by_category, name='category'),
        path('author/',views.by_author, name='author'),
    ]
