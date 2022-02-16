from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    # class Meta(UserCreateSerializer.Meta):
    #     model = User
    #     fields = ('id','email','first_name', 'last_name','mobile','is_active', 'password')
    pass


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = '__all__'