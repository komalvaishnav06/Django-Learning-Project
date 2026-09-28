from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField() #in bracket we can also write (default=18)
    email = models.EmailField(null=True , blank=True)
    address = models.TextField(null=True , blank=True)
    # image = models.ImageField()
    