from django.db import models

# Create your models here.

class School(models.Model):
    school_name=models.CharField(max_length=100)
    school_code=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    total_students=models.PositiveIntegerField()

class Students(models.Model):
    name=models.CharField(max_length=100)
    std=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
