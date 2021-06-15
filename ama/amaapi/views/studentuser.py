from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from amaapi.models import Event, Admin, Game

class StudentUserView(ViewSet):




class LessonNotesSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    organizer = StudentUserSeralizer(many=False)
    
    class Meta:
        model = LessonNotes
        fields = ['date', 'scale_notes', 'memory_notes', "song1_notes", "song2_notes"]
    