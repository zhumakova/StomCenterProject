from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class DoctorDay(models.Model):
    doctor=models.ForeignKey(User,on_delete=models.CASCADE)
    day=models.ForeignKey(Day,on_delete=models.CASCADE)

class Order(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='clients')
    day = models.ForeignKey(Day,on_delete=models.CASCADE)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctors')
    date_created = models.DateTimeField(auto_now_add=True)
