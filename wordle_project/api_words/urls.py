from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_words import views

router = DefaultRouter()
router.register(r'words', views.WordViewSet, basename='words')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
