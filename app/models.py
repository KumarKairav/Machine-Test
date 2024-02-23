from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    assigned_users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    