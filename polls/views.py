from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employs
from .serelizer import empSerel
class empList(APIView):
    def get(self,request):
        emp1 = employs.objects.all()
        sereliz = empSerel(emp1,many=True)
        return Response(sereliz.data)
    def post(self):
        pass



# Create your views here.
