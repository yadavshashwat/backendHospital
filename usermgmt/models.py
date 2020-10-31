from django.db import models
import json
from django.contrib.auth.models import AbstractUser
from overall.models import BaseModel
# Create your models here.

user_type = ['doctor','nurse','other']

class Hospital(BaseModel):
    name = models.CharField(max_length=50)
    def __str__(self):
        return json.dumps({'id':self.id,'name':self.name})

class HospitalUser(BaseModel):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    hospital = models.ForeignKey(Hospital,
                                on_delete=models.CASCADE,
                                null=False)
    email = models.CharField(max_length=50, null=True)
    secret_string = models.CharField(max_length=20, null=True)
    auth_token    = models.CharField(max_length=20, null=True)
    is_super_user = models.BooleanField(default=False)
    user_type = models.CharField(max_lenght=20)
    active = models.BooleanField(default=True)  
    # define user access list
    has_opd_mgmt = models.BooleanField(default=False)
    def __str__(self):
        return json.dumps({'id':self.id,'name':self.name})
    
class PatientUser(BaseModel):
    name = models.CharField(max_length=50)
    uin_number = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    dob = models.DateField()
    attendant_name = models.CharField(max_length=50)
    attendant_number = models.IntegerField()




