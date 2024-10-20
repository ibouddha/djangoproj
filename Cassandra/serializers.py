from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    titre = serializers.CharField(max_length=100)
    contenu = serializers.CharField()