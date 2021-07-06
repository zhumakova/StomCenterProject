from django.contrib import admin
from .models import *
admin.site.register(Day)

class DayDoctorDisplay(admin.ModelAdmin):
    list_display = ['day','doctor']

admin.site.register(DoctorDay,DayDoctorDisplay)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'doctor', 'day', 'date_created']
    readonly_fields = ['date_created']


admin.site.register(Order, OrderAdmin)