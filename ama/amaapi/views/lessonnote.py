"""View module for handling requests about games"""
from amaapi.models import StudentUser, LessonNotes
from django.core.exceptions import ValidationError
from rest_framework import fields, status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

class LessonNoteView(ViewSet):
    """The Allegro Music Academy Student Lesson Notes"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Lessonnotes instance
        """
        # Uses the token passed in the `Authorization` header
        #Line22 holds the power to make adjustments
        adminuser = Admin.objects.get(user=request.auth.user)

            # Create a new Python instance of the Game class
            # and set its properties from what was sent in the
            # body of the request from the client.
            
        notes = LessonNotes()
        notes.date = request.data["date"]
        notes.scale_notes = request.data["scale_notes"]
        notes.memory_notes = request.data["memory_notes"]
        notes.song1_notes = request.data["song1_notes"]
        notes.song2_notes = request.data["song2_notes"]
        
        
        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameTypeId` in the body of the request.
        lessonuser = StudentUser.objects.get(pk=request.data["student_userId"])
        notes.student_user = lessonuser

        try:
            notes.save()
            serializer = LessonNotesSerializer(notes, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class UserSerializer:
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class StudentUserSeralizer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = StudentUser
        fields = ['User']

class LessonNotesSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    organizer = StudentUserSeralizer(many=False)
    
    class Meta:
        model = LessonNotes
        fields = ['date', 'scale_notes', 'memory_notes', "song1_notes", "song2_notes"]
