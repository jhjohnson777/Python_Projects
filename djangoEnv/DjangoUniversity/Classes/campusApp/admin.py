from django.contrib import admin
from .models import UniversityCampus #imports UniversityCampus from models in the same app

# Register your models here.
admin.site.register(UniversityCampus) #Registers class