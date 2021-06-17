from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    studio_name = models.TextField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)