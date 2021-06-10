from django.db.models.deletion import CASCADE
from django.db import models


class Competitions(models.Model):

    date = models.DateField()
    name_of_comp = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    student_user =  models.ForeignKey("StudentUser", on_delete=CASCADE)
    admin = models.ForeignKey("Admin", on_delete=models.DO_NOTHING, null=True)
    award = models.ForeignKey("Awards", on_delete=CASCADE)
    