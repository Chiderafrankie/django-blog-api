from django.urls import path
from .views import RegisterView, AuthorProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('authors/<str:username>/', AuthorProfileView.as_view(), name='author-profile'),
]