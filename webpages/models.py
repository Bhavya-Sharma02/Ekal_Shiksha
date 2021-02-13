from django.db import models
from django.urls import reverse

class student(models.Model,):
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length = 100)
    Number=models.CharField(max_length = 10)
    Class=models.IntegerField()
    Course=models.CharField(max_length=30)
    Information=models.CharField(max_length=300)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('index')
