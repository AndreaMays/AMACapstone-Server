from django.db import models

class Admin(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    studio_name = models.TextField(max_length=250)
