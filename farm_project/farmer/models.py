from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Farmer(models.Model):
    """ models that defines a single farmer record """
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    TITLE = (
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('dr', 'Dr'),
        ('prof', 'Prof'),
    )

    title = models.CharField(max_length=5, choices=TITLE)
    name = models.CharField(max_length=256)
    surname = models. CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField()
    national_id = models.CharField(max_length=30)
    phone = models.CharField(max_length=16)
    email =models.EmailField()
    farm = models.TextField()

    def list_products(self, limit=3):
        """Returns a list of products for given farmer."""
        return Product.objects.filter(farmer=self).order_by('name')[:limit]

    def list_products_with_term(self, term):
        """this list out a list of products by name eg, all apples."""
        products = self.products(-1)
        matching = []
        for prod in products:
            if term in prod.name:
                matching.append(term)
        return matching

    def __str__(self):
        return 'Farmer: {name} {surname} ({birthdate})'.format(
        name = self.name,
        surname=self.surname,
        birthdate=self.date_of_birth 
        )

        #'Farmer<{name} {surname} ({birthdate})>'.format
        #name = self.name,
        #surname=self.surname,
        #birthdate=self.date_of_birth        self.name,
        #self.surname,
        #self.date_of_birth)



class Product(models.Model):
    """attributes include
    Category 'the catagory of that specific product'
    Name 'name of the product being sold'
    Description 'eg color of the apples etc'
    Quantity
    Unit
    Grade
    Availability"""

    CATEGORY = (
        ('d', 'Dairy'),
        ('f', 'Fruits'),
        ('v', 'Vegetables'),
        ('g', 'Grains'),
        ('o', 'other'),
        )
    
    UNIT = (
      ('gram', 'Kg'),
      ('liter', 'liter'),
      ('item', 'Item'),
    )
    
    GRADE = (
      ('1', 'Bad'),
      ('2', 'Somewhat good'),
      ('3', 'good'),
      ('4', 'very good'),
      ('5', 'Top quality'),
    )
    
    farmer = models.ForeignKey('Farmer', on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY, blank=False, null=True)
    name = models.CharField(help_text='enter the name of your product eg apples', max_length=128)
    description = models.TextField(help_text='discribe your product eg. my apples are red')
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNIT)
    grade = models.CharField(max_length=1, choices=GRADE)
    available = models.BooleanField()


    class meta:
        manage = True

    def __str__(self):
        return self.name
    









# Create your models here.
