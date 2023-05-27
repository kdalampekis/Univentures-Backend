# serializers.py
from rest_framework import serializers
from .models import User, UsersCategories, Volunteer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class UsersCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersCategories
        fields = ('user', 'categories')


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ('position', 'user', 'comment')
