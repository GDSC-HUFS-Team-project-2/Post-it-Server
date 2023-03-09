from rest_framework import serializers
from .models import User, Note, PostIt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("__all__")

class PostItSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostIt
        fields = ("__all__")