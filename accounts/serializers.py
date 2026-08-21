from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'created_at']


class AuthorProfileSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']

    def get_posts(self, obj):
        published_posts = obj.posts.filter(status='published')
        return AuthorPostSerializer(published_posts, many=True).data