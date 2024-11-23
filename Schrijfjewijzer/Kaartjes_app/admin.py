from django.contrib import admin
from .models import kind_Schoolvakken

@admin.register(kind_Schoolvakken)
class kind_SchoolvakkenAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('naam', 'Rekenen', 'Taal', 'Spelling', 'Technisch_lezen', 'Overig')
    
    # Fields to search for in the admin list view
    search_fields = ('naam', 'Rekenen', 'Taal', 'Spelling', 'Technisch_lezen', 'Overig')
    
    # Fields to filter by in the admin list view
    list_filter = ('Rekenen', 'Taal', 'Spelling')
