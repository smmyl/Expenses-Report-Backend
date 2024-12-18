from django.db import models

class Names(models.Model):
    names = models.CharField(max_length=32)