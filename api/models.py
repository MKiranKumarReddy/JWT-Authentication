from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(blank=True, max_length=125)
    salary = models.PositiveIntegerField()
    hr = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
