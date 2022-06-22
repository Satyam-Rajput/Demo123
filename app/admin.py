from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    pass


