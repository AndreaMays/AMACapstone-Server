from django.db.models.deletion import CASCADE
from django.db import models


class LessonNotes(models.Model):

    date = models.DateField()
    scale_notes = models.TextField(max_length=255)
    memory_notes = models.TextField(max_length=255)
    song1_notes = models.TextField(max_length=255)
    song2_notes = models.TextField(max_length=255)
    student_user =  models.ForeignKey("StudentUser", on_delete=CASCADE)
    admin = models.ForeignKey("Admin", on_delete=models.DO_NOTHING, null=True)