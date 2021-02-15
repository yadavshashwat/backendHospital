from django.db import models
import json
from overall.models import BaseModel
# Create your models here.

class PatientUser(BaseModel):
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    phone_number = models.IntegerField(null=False)
    address = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    pincode = models.IntegerField(null=False)
    patientid = models.IntegerField(null=False)
    dob = models.DateField(null=True)
    def __str__(self):
        return json.dumps({'id':self.id,'name':self.first_name})




