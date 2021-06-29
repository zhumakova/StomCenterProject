from django.contrib import admin
from .models import *
admin.site.register(Day)

class DayDoctorDisplay(admin.ModelAdmin):
    list_display = ['day','doctor']

admin.site.register(DoctorDay,DayDoctorDisplay)
