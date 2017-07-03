# string related field -> serializer relations
from .models import *
from rest_framework import serializers


# class MovieSerializer(serializers.HyperlinkedModelSerializer):
class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    director = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'director', 'year', 'actors')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

