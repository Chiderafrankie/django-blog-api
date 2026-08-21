from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, AuthorProfileSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class AuthorProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorProfileSerializer
    lookup_field = 'username'