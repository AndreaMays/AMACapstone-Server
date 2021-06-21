"""View module for handling requests about competitions"""
from amaapi.models.awards import Awards
from typing import ContextManager
from amaapi.models import StudentUser, LessonNotes, Admin, studentusers, Competitions
from django.core.exceptions import ValidationError
from rest_framework import fields, status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

class StudentCompetitionList(ViewSet):

    def list(self, request):
#    line 80 in paranthesis is authenticating the admin and then setting that to "admin" inside the paranthesis
# then everything on the right side is being set to the variable name "adminuser"
        studentuser = StudentUser.objects.get(user=request.auth.user)
        competitions = Competitions.objects.filter(student_user=studentuser)
        # user = User.objects.get(user=request.auth.user)
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
        model = Competitions
        fields = ['date', 'name_of_comp', 'score', "award", "student_user"]

class AwardSeralizer(serializers.ModelSerializer):
    competitontracker = CompetitionSerializer()
    class Meta:
        model = Awards
        fields = ['date', "name_of_comp", "type_of_award", "admin", "student_user"]  