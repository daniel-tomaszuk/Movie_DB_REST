# string related field -> serializer relations

from .models import *
from rest_framework import serializers


# class MovieSerializer(serializers.HyperlinkedModelSerializer):
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'director', 'year', 'actors')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
