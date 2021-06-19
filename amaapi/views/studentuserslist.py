from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from amaapi.models import Admin, LessonNotes, StudentUser

class StudentUserListView(ViewSet):

    def list(self, request):
#    line 14 in paranthesis is authenticating the user and then setting that to "user" inside the paranthesis
# then everything on the right side is being set to the variable name "studentuser"
        studentuser = User.objects.filter(is_superuser=False)

        # notes = LessonNotes.objects.filter(student_user=studentuser)
# line 15 (above) inside the paraenthsis, is filtering the LessonNotes object by the dot notation on line 14
# then(inside the paraenthis) i am setting the authenticated user variable name from 14 equal to "student_user" which is one of the key
        serializer = UserSerializer(
            studentuser, many=True, context={'request': request})
        return Response (serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id']