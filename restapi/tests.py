from django.test import TestCase
from restapi import models
from django.urls import reverse

# Create your tests here.

class TestModels(TestCase):
    def test_expense(self):
        expense= models.expense.objects.create(amount_in_INR=1500, merchant="amazon", brand="boat", description="earpods", category="gadgets")
        inserted_expense=models.Exepense.objects.get(pk=expense.id)

        self.assertEqual(1500, inserted_expense.amount_in_INR)
        self.assertEqual(1500, inserted_expense.merchant)
        self.assertEqual(1500, inserted_expense.brand)
        self.assertEqual(1500, inserted_expense.description)
        self.assertEqual(1500, inserted_expense.category)

class TestView(TestCase):
    def test_expense_create(self):
        payload={
            "amount_in_INR": 3500.00,
            "merchant": 'flipkart',
            "brand": 'nike',
            "description":'shoes',
            "category": 'footwear'
        }

        rest=self.client.post(reverse("restapi:Expense-List-Create"), payload, format='json')
        self.assertEqual(201,rest.status_code)
        json_rest=rest.json()
        self.assertEqual(payload["amount_in_INR"]), json_rest["amount_in_INR"]
        self.assertEqual(payload["merchant"], json_rest["merchant"])
        self.assertEqual(payload["brand"], json_rest["brand"])
        self.assertEqual(payload["description"], json_rest["description"])
        self.assertEqual(payload["category"], json_rest["category"])
        self.assertIsInstance(json_rest["id"],int) 
    
    def test_expense_list(self):
        rest=self.client.post(reverse("restapi:Expense-List-Create"),format='json')

        self.assertEqual(200,rest.status_code)

        json_rest=rest.json()

        self.assertIsInstance(json_rest,list)

        expenses=models.Expense.objects.all()

        self.assertEqual(len(expenses))
    

    def test_expense_create_required_fields_missing(self):
        payload={
            "merchant": 'flipkart',
            "brand": 'nike',
            "description":'shoes',
            "category": 'footwear'
        }

        rest=self.client.post(reverse("restapi:expense-list-create"),payload, format="json")

        self.assertEqual(400, rest.status_code)

    
    def test_expense_retrieve(self):
        expense=models.Expense.objects.create(amount_in_INR=1000, merchant="ram", description="loan", category="transfer")
        rest=self.client.get(reverse("restapi:expense-retrieve-delete", args=[expense.id], format="json"))

        self.assertEqual(200,rest.status_code)

        json_rest= rest.json()

        self.assertEqual(expense.id, json_rest["id"])
        self.assertEqual(expense.amount_in_INR, json_rest["amount_in_INR"])
        self.assertEqual(expense.merchant, json_rest["merchant"])
        self.assertEqual(expense.description, json_rest["description"])
        self.assertEqual(expense.category, json_rest["category"])

    def text_expense_delete(self):
        expense=models.Expense.objects.create(amount_in_INR=1000, merchant="sham", description="loan", category="transfer")
        rest=self.client.delete(reverse("restapi:expense-retrieve-delete", args=[expense.id], format="json"))

        self.assertEqual(204, rest.status_code)
        self.assertFalse(models.Expense.objects.filter(pk=expense.id).exists())

