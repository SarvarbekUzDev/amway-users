from django.contrib import admin

from .models import Workers, Products


# Register your models here.

@admin.register(Workers)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name','mail',)
    list_filter = ('name','mail',)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','worker','user','active',)
    list_filter = ('name','worker','user','active',)