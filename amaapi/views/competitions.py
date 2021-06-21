"""View module for handling requests about games"""
from amaapi.models.awards import Awards
from typing import ContextManager
from amaapi.models import StudentUser, LessonNotes, Admin, studentusers, competitontracker
from django.core.exceptions import ValidationError
from rest_framework import fields, status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

class CompetitionViews(ViewSet):
    """The Allegro Music Academy Student Lesson Notes"""
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Competitions instance
        """
        # Uses the token passed in the `Authorization` header
        #Line22 holds the power to make adjustments
        adminuser = Admin.objects.get(user=request.auth.user)

            # Create a new Python instance of the Game class
            # and set its properties from what was sent in the
            # body of the request from the client.
            
        competitions = competitontracker()
        competitions.date = request.data["date"]
        competitions.name_of_comp = request.data["name_of_comp"]
        competitions.score = request.data["score"]

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameTypeId` in the body of the request.
        lessonuser = StudentUser.objects.get(pk=request.data["student_userId"])
        competitions.student_user = lessonuser
        competitions.admin = adminuser

        try:
            competitions.save()
            serializer = CompetitionSerializer(competitions, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET request for single competition entrance
       Returns: Response -- JSON serialized instance 
        """
        try:
            competitons = competitontracker.objects.get(pk=pk)
            serializer = CompetitionSerializer(competitons, context={'request': request})
            return Response(serializer.data)
        except Exception:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """This is the DELETE request for a single competition
        Returns: Response -- 200, 404, or 500 status code
        """
        try:
            competitions = competitontracker.objects.get(pk=pk)
            competitions.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except LessonNotes.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
#    line 80 in paranthesis is authenticating the admin and then setting that to "admin" inside the paranthesis
# then everything on the right side is being set to the variable name "adminuser"
        adminuser = Admin.objects.get(user=request.auth.user)
        competitions = competitontracker.objects.filter(admin=adminuser)
        user = User.objects.get(user=request.auth.user)
# line 81 (above) inside the paraenthsis, is filtering the LessonNotes object by the dot notation on line 14
# then(inside the paraenthis) i am setting the authenticated user variable name from 14 equal to "student_user" which is one of the key
        serializer = CompetitionSerializer(
            competitions, many=True, context={'request': request})
        return Response (serializer.data)

        # serializer = UserSerializer(
        #     user, many = True, context={'request': request})
        # return Response (serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id']

class StudentUserSeralizer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentUser
        fields = ['user']

class CompetitionSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    student_user = StudentUserSeralizer(many=False)
    
    class Meta:
        model = competitontracker
        fields = ['date', 'name_of_comp', 'score', "award", "student_user"]

class AwardSeralizer(serializers.ModelSerializer):
    competitontracker = CompetitionSerializer()
    class Meta:
        model = Awards
        fields = ['date', "name_of_comp", "type_of_award", "admin", "student_user"]    