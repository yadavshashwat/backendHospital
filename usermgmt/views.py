from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.paginator import Paginator

# import math

from usermgmt.serializers import *
from overall.views import *


@api_view(['GET', 'POST', 'DELETE'])
def hospital_list(request):
    if request.method == 'GET':
        hospitals = Hospital.objects.all()

        # setting up filters
        name = request.GET.get('name', None)
        if name is not None:
            hospitals = hospitals.filter(name__icontains=name)
        
        # Setting up pagination
        pagination_out = pagination(object=hospitals,request=request)
        hospital_serializer = HospitalSerializer(pagination_out['object'], many=True)
        
        num_pages = pagination_out['num_pages']
        total_records = pagination_out['total_records']
        data = hospital_serializer.data
        filters = {}
        success = True
        message = "Found Hospital Records"

        return JsonResponse(
            {
                'data':data,
                'success':success,
                'filters':filters,
                'num_pages':num_pages,
                'total_records':total_records,
                'message':message
            }
            , safe=False)
 
    elif request.method == 'POST':
        hospital_data = JSONParser().parse(request)
        try:
            hospital_data['name'] = cleanstring(hospital_data['name'].lower())
            hospital_data['address'] = cleanstring(hospital_data['address'].lower())
            hospital_data['city'] = cleanstring(hospital_data['city'].lower())
            hospital_data['state'] = cleanstring(hospital_data['state'].lower())
        except:
            None

        hospital_serializer = HospitalSerializer(data=hospital_data)
        
        if hospital_serializer.is_valid():
            hospital_serializer.save()
            success = True
            message = "Hospital Created!"
            return JsonResponse({
                'data':hospital_serializer.data,
                'success':True,
                'message':message
            }, status=status.HTTP_201_CREATED) 
        
        else:
            success = False
            message = "Invalid Serializer!"
            return JsonResponse({
                'errors':hospital_serializer.errors,
                'success':success,
                message: message
            }
            , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Hospital.objects.all().delete()
        return JsonResponse({
            'success':True,
            'message': '{} Hospitals were deleted successfully!'.format(count[0])
            }, status=status.HTTP_204_NO_CONTENT)
 
 
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
    
        
    
