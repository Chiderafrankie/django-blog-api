from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import TagViewSet, PostViewSet, HomeView, SearchView, Trendingview

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls + [
    path('home/', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('trending/', Trendingview.as_view(), name='trending'),
]