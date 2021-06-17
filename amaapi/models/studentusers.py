from django.db import models
from django.contrib.auth.models import User

class StudentUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent_first_name = models.CharField(max_length=50)
    parent_last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    birth_date = models.CharField(max_length=50)
    admin = models.ForeignKey("Admin", on_delete=models.DO_NOTHING, null=True)