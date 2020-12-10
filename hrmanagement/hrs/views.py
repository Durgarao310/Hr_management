from hrs.models import Employee, Hr
from hrs.serializers import EmployeeSerializer, HrSerializer
from rest_framework import generics
from django.shortcuts import render
from hrs.permissions import IsOwnerOrReadOnly
from rest_framework import permissions

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly,]
    def get_queryset(self):
        return Employee.objects.filter(employee_hr=self.request.user)
    



class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly,]
    
    def get_queryset(self):
            return Employee.objects.filter(employee_hr=self.request.user)

