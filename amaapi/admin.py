from django.contrib import admin
from amaapi.models import LessonNotes, StudentUser, Competitions, Awards, Admin

admin.site.register(LessonNotes)
admin.site.register(StudentUser)
admin.site.register(Competitions)
admin.site.register(Awards)
admin.site.register(Admin)