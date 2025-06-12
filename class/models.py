from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BioData(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.IntegerField()
    Date_of_Birth = models.DateField()
    class_section = models.CharField(max_length=20)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    student_image = models.FileField(upload_to='media', null=True, blank=True)

    