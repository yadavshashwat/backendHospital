"""backendHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include 
from usermgmt.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'crud_exchange/', views.crud_exchange, name='crud_exchange'),
    # version 1 apis
    url(r'^api/v1/hospitals$', hospitalMgmt.object_list_v1),
    url(r'^api/v1/hospitals/(?P<id>[0-9]+)$', hospitalMgmt.object_detail_v1),

    # url(r'^', include('usermgmt.urls')),

]



 
