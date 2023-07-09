from django.test import TestCase
from restapi import models

# Create your tests here.

class testModels(TestCase):
    def test_expense(self):
        expense= models.expense.objects.create(amount_in_INR=1500, merchant="amazon", brand="boat", description="earpods", category="gadgets")
        inserted_expense=models.Exepense.objects.get(pk=expense.id)

        self.assertEqual(1500, inserted_expense.amount_in_INR)
        self.assertEqual(1500, inserted_expense.merchant)
        self.assertEqual(1500, inserted_expense.brand)
        self.assertEqual(1500, inserted_expense.description)
        self.assertEqual(1500, inserted_expense.category)




