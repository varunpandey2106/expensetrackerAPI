from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models, serializers
from django.forms.models import model_to_dict
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView

# Create your views here.

class ExpenseListCreate(ListCreateAPIView):
    serializer_class=serializers.Expense
    queryset=models.Expense.objects.all()
  
    
class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class=serializers.Expense
    queryset=models.Expense.objects.all()

    
    
    
        

