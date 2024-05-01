from django.http import JsonResponse
from django.shortcuts import render

from API.models import Student


# Create your views here.


def getStudents(request):
    students = Student.objects.all()
    data = [{'name': student.name, 'roll': student.roll, 'city': student.city} for student in students]

    return JsonResponse(data, safe=False)

