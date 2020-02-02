from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()