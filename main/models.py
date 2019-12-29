from django.db import models

from accounts.models import Client


class Article(models.Model):
    name = models.CharField(max_length = 100)
    short_text = models.TextField()
    text = models.TextField()

    publication_date = models.DateTimeField(null = True)

    author = models.ForeignKey(Client, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.name
