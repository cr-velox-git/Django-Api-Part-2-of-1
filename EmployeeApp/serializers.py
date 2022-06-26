from dataclasses import field
from rest_framework import serializers
from EmployeeApp.models import Employees,Departments

#serializer  for our model
class DepartmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        field = ('DepartmentId',
                'DepartmentName')
        fields = '__all__'


class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        field = ('EmployeeId',
                'EmployeeName',
                'DepartmentName',
                'DateOfJoining',
                'PhotoFileName'
                )
        fields = '__all__'