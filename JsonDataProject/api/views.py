import json

from django.shortcuts import render
from django.http import HttpResponse

from .sample import get_source
from .models import Employee, ActivityPeriods


def index(request):
    """:param
    return: list of employees
    renders list of employees to index page"""
    employee = Employee.objects.all()
    return render(request, 'api/index.html', {"employee_list": employee})


def read_data_from_file(request):
    """:param: path sources
    return: success"""
    get_source('api/json_data_file')

    return HttpResponse("success")
