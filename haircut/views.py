from django.shortcuts import render
from rest_framework import generics

from haircut.serializers import WorkerSerializer
from .models import Worker
from rest_framework.response import Response
from rest_framework.views import APIView


# class HaircutAPIView(generics.ListAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
    
class HaircutAPIView(generics.ListAPIView):
    def get(self, request):
        return Response({'name': 'Anton'})
    
    def post(self, request):
        return Response({'sername': 'Ivanov'})