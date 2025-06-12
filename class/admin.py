from django.contrib import admin
from .models import BioData
# Register your models here.
class BioDataAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'age', 'Date_of_Birth', 'class_section')
    list_filter = ('age', 'class_section')
    
admin.site.register(BioData, BioDataAdmin)