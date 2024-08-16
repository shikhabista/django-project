from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=1, null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    faculty_choices = (
        ('BCA', 'BCA'),
        ('BBA', 'BBA'),
    )
    faculty = models.CharField(max_length=10, choices=faculty_choices)

    def __str__(self):
        return self.name
