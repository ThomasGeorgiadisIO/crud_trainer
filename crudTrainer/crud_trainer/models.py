from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=10)
