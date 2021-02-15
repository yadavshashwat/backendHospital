from django.db import models
import json
from overall.models import BaseModel
# Create your models here.

user_type = ['doctor','nurse','other']

class Hospital(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    is_opd_active = models.BooleanField(default=True)
    sms_balance = models.IntegerField(default=0)
    email_balance = models.IntegerField(default=0)
    def __str__(self):
        return json.dumps({'id':self.id,'name':self.name})

class HospitalUser(BaseModel):
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    phone_number = models.IntegerField(null=False)
    hospital = models.ForeignKey(Hospital,
                                on_delete=models.CASCADE,
                                null=False)
    email = models.CharField(max_length=50, null=True)
    secret_string = models.CharField(max_length=20, null=True)
    auth_token    = models.CharField(max_length=20, null=True)
    is_super_user = models.BooleanField(default=False)    
    otp = models.IntegerField(null=True)
    otp_time = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)  
    # define user access list
    # access types = r, rw, a | r = read, rw = readwrite, a = admin (delete priviledges)
    has_opd_mgmt_acces = models.BooleanField(default=False)
    opd_mgmt_access_type = models.CharField(max_length=2, default="r")
    def __str__(self):
        return json.dumps({'id':self.id,'name':self.first_name})
    
# class PatientUser(BaseModel):
#     name = models.CharField(max_length=50)
#     phone_number = models.IntegerField()
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     pincode = models.IntegerField()
#     dob = models.DateField()
#     attendant_name = models.CharField(max_length=50)
#     attendant_number = models.IntegerField()
#     def __str__(self):
#         return json.dumps({'id':self.id,'name':self.name})




