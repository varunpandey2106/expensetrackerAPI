from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from restapi import models
from django.forms.models import model_to_dict
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Expense




# Create your views here.

class ExpenseListCreate(ListCreateAPIView):
    serializer_class=serializers.Expense
    queryset=models.Expense.objects.all()
    filterset_fields=["category", "merchant"]
    permission_classes= [IsAuthenticated]
  
    
class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class=serializers.Expense
    queryset=models.Expense.objects.all()

    
    
    
        

