from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
   
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
 

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_time = models.DateTimeField(auto_now_add=True)
    checked_in_time = models.DateTimeField(null=True, blank=True)
    condition_checked_out = models.CharField(max_length=100)
    condition_checked_in = models.CharField(max_length=100, null=True, blank=True)

