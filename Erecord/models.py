from django.db import models
from django.contrib.auth.models import User# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emcode = models.CharField(max_length=50)
    emdept = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50)
    joiningdate = models.DateField(null=True)
    def __str__(self):
        return self.user.username