from rest_framework import serializers 
from usermgmt.models import *
 
 
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id',
                  'name',
                  'address',
                  'city',
                  'state',
                  'pincode',
                  'is_opd_active',
                  'sms_balance',
                  'email_balance'
                  )

