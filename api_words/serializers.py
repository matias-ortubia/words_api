from rest_framework import serializers
from api_words.models import Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'length', 'language']