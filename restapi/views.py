from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models
from django.forms.models import model_to_dict

# Create your views here.

class ExpenseListCreate(APIView):
    def get(self,request):
        expenses=models.Expense.objects.all()
        all_expenses=[model_to_dict(expenses) for expense in expenses]
        return Response(all_expenses,status=200)


    def post(self,request):
        amount_in_INR=request.data("amount_in_INR")
        merchant=request.data("merchant")
        brand=request.data("brand")
        description=request.data("description")
        category=request.data("catgeory")

        expense=models.Expense.objects.create(amount_in_INR='amount_in_INR',merchant='merchant',brand='brand',description='description' ,catgeory='category' )
        return Response(model_to_dict(expense, status=201))
