from django.db import models
from django.contrib.auth.models import AbstractUser # customizing the user model 
from PIL import Image
from django.conf import settings


# Create your models here.


class Hr(AbstractUser):
    phone    = models.IntegerField(unique=True, null=True)
    email    = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=100, unique=True)
    hr_image = models.ImageField(upload_to='hr_profile_pics', null=True, blank=True)



    USERNAME_FIELD = 'email' # user login field  
    REQUIRED_FIELDS = ['username','phone']

    def __str__(self):
        return self.username


class Employee(models.Model):
    employee_hr              = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    employee_name            = models.CharField(max_length=150)
    employee_surname         = models.CharField(max_length=150)
    employee_phone_num       = models.IntegerField()
    employee_joinded         = models.DateTimeField(auto_now_add=True, blank=True)
    employee_image           = models.ImageField(upload_to='employee_profile_pics', null=True, blank=True)
    employee_address         = models.TextField()
    employee_position        = models.CharField(max_length=100)
    employee_salary          = models.IntegerField()