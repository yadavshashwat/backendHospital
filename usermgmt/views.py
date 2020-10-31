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
        obj =             {
                'data':data,
                'success':success,
                'filters':filters,
                'num_pages':num_pages,
                'total_records':total_records,
                'message':message
            }

        return JsonResponse(obj, safe=False)
 
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
            data = hospital_serializer.data
            obj= {
                'data': data,
                'success':True,
                'message':message
            }
            return JsonResponse(obj, status=status.HTTP_201_CREATED) 
        
        else:
            success = False
            message = "Invalid Serializer!"
            errors = hospital_serializer.errors
            obj = {
                'errors': errors,
                'success':success,
                'message': message
            }
            return JsonResponse(obj, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Hospital.objects.all().delete()
        success = True
        message = '{} Hospitals were deleted successfully!'.format(count[0])
        obj= {
            'success':True,
            'message': message
            }
        return JsonResponse(obj, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def hospital_detail(request, id):
    try: 
        hospital = Hospital.objects.get(id=id) 
    except Hospital.DoesNotExist: 
        message = 'The hospital does not exist'
        success = False
        obj = {
                'message': message,
                'success': success
              }
        return JsonResponse(obj, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        hospital_serializer = HospitalSerializer(hospital) 
        message = "Hospital Found!"
        success = True
        data = hospital_serializer.data
        obj ={
                'data':data,
                'success':success,
                'message':message
            }
        return JsonResponse(obj) 
 
    elif request.method == 'PUT': 
        hospital_data = JSONParser().parse(request) 
        hospital_serializer = HospitalSerializer(hospital, data=hospital_data) 
        if hospital_serializer.is_valid(): 
            hospital_serializer.save() 
            success = True
            data = hospital_serializer.data
            message = "Hospital Updated!"
            obj ={
                'data':data,
                'success':success,
                'message':message
            }
            return JsonResponse(obj) 
        else:
            success = False
            errors = hospital_serializer.errors
            message = "Unable to update hospital"
            obj = {
                'success':False,
                'errors': errors,
                'message':message
            }
        return JsonResponse(obj, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        hospital.delete() 
        success = True
        message = 'Hospital was deleted successfully!'
        obj= {
            'success':True,
            'message': message
            }

        return JsonResponse(obj, status=status.HTTP_204_NO_CONTENT)
    
        
    
