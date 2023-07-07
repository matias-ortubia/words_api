from django.shortcuts import render
from rest_framework import viewsets
from api_words.models import Word
from api_words import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = serializers.WordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def index(request):
    return render(request, 'index.html')