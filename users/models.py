from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db import models

# Create your models here.
class Owner(AbstractUser):
    username=None
    email=models.EmailField(_("Email Address"),unique=True)
    phone_number=models.IntegerField(null=False)
    owner_ID=models.IntegerField(null=False, unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        app_label="Owner"
        verbose_name_plural="Owners"


class Rider(models.Model):
    first_name=models.CharField(max_length=15, null=False)
    last_name=models.CharField(max_length=15,null=False)
    # gender=models.CharField(max_length=8, null=False)
    ID_Number=models.IntegerField(null=False,unique=True)
    brand=models.CharField(max_length=15,null=False,blank=True)
    model=models.CharField(max_length=10,null=False,blank=True)
    number_plate=models.CharField(max_length=10,null=False,primary_key=True,default="KMTC 123G")
    offence_count=models.IntegerField(null=False,default=0)
    # employer=models.ForeignKey(Owner,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Offence(models.Model):
    time=models.DateTimeField(auto_now=True,null=False)
    longitude=models.FloatField(null=True)
    latitude=models.FloatField(null=True)
    speed=models.FloatField(null=True)
    speed_limit=models.IntegerField(null=True)
    vehicle=models.ForeignKey(Rider,on_delete=models.CASCADE,null=False)

# class vehicle(models.Model):
#     brand=models.CharField(max_length=15,null=False)
#     model=models.CharField(max_length=10,null=False)
#     number_plate=models.CharField(max_length=10,null=False,unique=True)
#     Rider=models.ForeignKey(Rider,on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.brand} {self.model} {self.number_plate}"
