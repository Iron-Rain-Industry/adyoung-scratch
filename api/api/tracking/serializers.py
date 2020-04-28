from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Set, Workout, Exercise

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ['exercise', 'reps', 'workout']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['workout', 'date']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['exercise', 'bodypart', 'description']