from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

    status = models.CharField(max_length=30, choices=[('a', 'Admin'), ('u', 'User')])
    account = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)
