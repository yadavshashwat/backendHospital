from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from usermgmt.models import *
from usermgmt.serializers import *
from rest_framework.decorators import api_view
from overall.views import *

@api_view(['GET', 'POST', 'DELETE'])
def hospital_list(request):
    if request.method == 'GET':
        hospitals = Hospital.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            hospitals = hospitals.filter(name__icontains=name)
        hospital_serializer = HospitalSerializer(hospitals, many=True)
        output = hospital_serializer.data
        filters = {}
        success = True
        return JsonResponse({'data':output,'success':success,'filters':filters}, safe=False)
 
    elif request.method == 'POST':
        hospital_data = JSONParser().parse(request)
        hospital_data['name'] = cleanstring(hospital_data['name'].lower())
        hospital_data['address'] = cleanstring(hospital_data['address'].lower())
        hospital_data['city'] = cleanstring(hospital_data['city'].lower())
        hospital_data['state'] = cleanstring(hospital_data['state'].lower())
        hospital_serializer = HospitalSerializer(data=hospital_data)
        if hospital_serializer.is_valid():
            hospital_serializer.save()
            return JsonResponse(hospital_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(hospital_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Hospital.objects.all().delete()
        return JsonResponse({'message': '{} Hospitals were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def hospital_detail(request, id):
    try: 
        hospital = Hospital.objects.get(id=id) 
    except Hospital.DoesNotExist: 
        return JsonResponse({'message': 'The hospital does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        hospital_serializer = HospitalSerializer(hospital) 
        return JsonResponse(hospital_serializer.data) 
 
    elif request.method == 'PUT': 
        hospital_data = JSONParser().parse(request) 
        hospital_serializer = HospitalSerializer(hospital, data=hospital_data) 
        if hospital_serializer.is_valid(): 
            hospital_serializer.save() 
            return JsonResponse(hospital_serializer.data) 
        return JsonResponse(hospital_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        hospital.delete() 
        return JsonResponse({'message': 'Hospital was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
    
