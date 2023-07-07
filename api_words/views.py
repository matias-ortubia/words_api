import random
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from api_words.models import Word
from api_words import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api_words.serializers import WordSerializer

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = serializers.WordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def random_word(request, letters = None):
    queryset = None
    if letters == None:
        queryset = Word.objects.all()

    else:
        queryset = Word.objects.filter(length=letters)

    random_word = random.choice(queryset)
    serializer = WordSerializer(random_word)
    return Response(serializer.data)

def index(request):
    return render(request, 'index.html')