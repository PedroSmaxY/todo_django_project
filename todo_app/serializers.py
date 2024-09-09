from rest_framework import serializers
from .models import User, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'user',
            'title',
            'description',
            'isCompleted',
            'created_date',
            'change_date',
        )


class TodoSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'isCompleted', 'created_date', 'change_date')


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializerForUser(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'todos',
        )
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True},
        }
