from rest_framework import serializers
from .models import Category, Tag, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    like_count = serializers.SerializerMethodField()
    read_time = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'excerpt', 'content', 'cover_image', 'author', 'author_username', 'category', 'category_name', 'tags', 'status', 'view_count', 'like_count', 'read_time', 'created_at', 'updated_at']
        read_only_fields = ['author', 'slug', 'view_count', 'created_at', 'updated_at']

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_read_time(self, obj):
        word_count = len(obj.content.split())
        minutes = max(1, round(word_count / 200))  
        return f"{minutes} min read"  # Assuming average reading speed of 200 words per minute