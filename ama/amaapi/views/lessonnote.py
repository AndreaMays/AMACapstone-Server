"""View module for handling requests about games"""
from amaapi.models import StudentUser, LessonNotes, Admin, studentusers
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
        notes.admin = adminuser

        try:
            notes.save()
            serializer = LessonNotesSerializer(notes, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET request for single lesson note
       Returns: Response -- JSON serialized instance 
        """
        try:
            lessonnote = LessonNotes.objects.get(pk=pk)
            serializer = LessonNotesSerializer(lessonnote, context={'request': request})
            return Response(serializer.data)
        except Exception:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """This is the DELETE request for a single note
        Returns: Response -- 200, 404, or 500 status code
        """
        try:
            lessonnote = LessonNotes.objects.get(pk=pk)
            lessonnote.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except LessonNotes.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
#    line 80 in paranthesis is authenticating the admin and then setting that to "admin" inside the paranthesis
# then everything on the right side is being set to the variable name "adminuser"
        adminuser = Admin.objects.get(user=request.auth.user)
        studentadminnotes = LessonNotes.objects.filter(admin=adminuser)
# line 81 (above) inside the paraenthsis, is filtering the LessonNotes object by the dot notation on line 14
# then(inside the paraenthis) i am setting the authenticated user variable name from 14 equal to "student_user" which is one of the key
        serializer = LessonNotesSerializer(
            studentadminnotes, many=True, context={'request': request})
        return Response (serializer.data)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id']

class StudentUserSeralizer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentUser
        fields = ['user']

class LessonNotesSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    student_user = StudentUserSeralizer(many=False)
    
    class Meta:
        model = LessonNotes
        fields = ['date', 'scale_notes', 'memory_notes', "song1_notes", "song2_notes", "student_user"]
