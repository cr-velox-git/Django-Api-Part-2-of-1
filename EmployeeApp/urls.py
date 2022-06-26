from django.urls import re_path as url
from API.settings import MEDIA_ROOT
from EmployeeApp import views

#for image
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns=[
    url(r'^department/$',views.departmentApi), 
    url(r'^department/([0-9]+)$', views.departmentApi), #this for delete

    url(r'^employee/$',views.employeeApi), 
    url(r'^employee/([0-9]+)$', views.employeeApi), #this for delete

    #for image
    url(r'^employee/save_file',views.SaveFile)
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)