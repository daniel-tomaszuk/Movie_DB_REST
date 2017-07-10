from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class MovieList(APIView):

    def get(self, request, format=None):
        """
        Gets all rows from Movies in DB, serializes it and return in response
        :param request:
        :param format:
        :return: Serialized Movies data
        """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Creates new Movie if POSTED data is valid
        :param request:
        :param format:
        :return:
        """
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):

    def get_object(self, pk):
        """
        Gets movie with id=pk from DB
        :param pk: primary key of row in Movie table
        :return: Movie object with ID = pk
        """
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """
        Gets, serializes and returns Movie object with  ID = id
        :param request:
        :param id:
        :param format:
        :return:
        """
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        """
        Gets and deletes Movie object with ID = id
        :param request:
        :param id: id of movie to be deleted (id in Movie table in DB)
        :param format:
        :return: 204 response -> no movie found
        """
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        """
        Updates Movie object with ID = id
        :param request:
        :param id: id of Movie object in DB
        :param format:
        :return: Updated data if provided data is valid or 404 error if
                 provided data is invalid
        """
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        """
        Not supported. To create new Movie use POST in MovieList class
        :param request:
        :param id:
        :param format:
        :return:
        """
        pass


class PersonList(APIView):

    def get(self, request, format=None):
        """
        Serializes and returns all people in DB
        :param request:
        :param format:
        :return: Serializes data of all people in DB
        """
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Creates new person if POSTED data is valid, returns 400 error if
        provided data is invalid.
        :param request:
        :param format:
        :return: Provided data if object was created or 400 error if provided
                 data was invalid
        """
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):

    def get_object(self, pk):
        """
        Gets Person's object from DB
        :param pk: primary key of Person row in DB
        :return: Person row with ID = pk
        """
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """
        Gets person (with ID = id), serializes it and returns
        :param request:
        :param id: id (primary key) of row in Person table
        :param format:
        :return: response with serialized object
        """
        person = self.get_object(id)
        serializer = PersonSerializer(person, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        """
        Deletes person with ID = id
        :param request:
        :param id: id of row in Person table
        :param format:
        :return: 204 error
        """
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        """
        Updates Person with ID = id
        :param request:
        :param id: id of row in Person table
        :param format:
        :return: Updated data if provided data is valid or 400 error if
                 if provided data is invalid
        """
        person = self.get_object(id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        """
        Not supported. To create new Person use POST in PersonList class
        :param request:
        :param id:
        :param format:
        :return:
        """
        pass

