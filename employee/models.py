from django.db import models

# Create your models here.
   
class Employee(models.Model): 
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)  
    age = models.IntegerField()
    email = models.EmailField(unique=True, max_length=25)
    mobile = models.CharField(unique=True, max_length=13)
    city = models.CharField(max_length=100)  
    salary = models.FloatField()

class Meta:
    db_table="empdata"
