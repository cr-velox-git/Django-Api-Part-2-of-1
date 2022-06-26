from urllib import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #so we can use it to allow other domain to acces it easly
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerilizer, EmployeeSerilizer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departmentApi(request,id= 0):
    if request.method=='GET':
        departments = Departments.objects.all()
        department_serilizer=DepartmentSerilizer(departments, many=True)
        return JsonResponse(department_serilizer.data,safe=False)
    elif request.method == 'POST':
        department_data=JSONParser().parse(request)
        department_serilizer = DepartmentSerilizer(data=department_data)
        if department_serilizer.is_valid():
            department_serilizer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method =='PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serilizer = DepartmentSerilizer(department,data=department_data)
        if department_serilizer.is_valid():
            department_serilizer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method =='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def employeeApi(request,id= 0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employee_serilizer=EmployeeSerilizer(employees, many=True)
        return JsonResponse(employee_serilizer.data,safe=False)
    elif request.method == 'POST':
        employee_data=JSONParser().parse(request)
        employee_serilizer = EmployeeSerilizer(data=employee_data)
        if employee_serilizer.is_valid():
            employee_serilizer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method =='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
        employee_serilizer = EmployeeSerilizer(employee,data=employee_data)
        if employee_serilizer.is_valid():
            employee_serilizer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method =='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file= request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)