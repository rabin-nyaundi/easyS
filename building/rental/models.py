from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    

class Building(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    location  = models.CharField(max_length =255, blank=False)
    owner = models.CharField(max_length = 255, blank=False)
    units_count = models.CharField(max_length = 255, blank=False)
    
    def __str__(self):
        return self.name
    
class Tenant(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length = 255, blank=False, unique=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    next_of_kin =  models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name
    
    
class BuildingTenant(models.Model):
    building =  models.ForeignKey(Building, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(auto_now_add=True)
    contract_amount =  models.IntegerField(blank=True)
    status = models.BooleanField(null = False)
    
    def __str__(self):
        return self.building
    
