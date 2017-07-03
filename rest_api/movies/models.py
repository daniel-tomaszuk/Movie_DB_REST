from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return '{}'.format(self.name)


class Movie(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='director', default=None)
    year = models.IntegerField()
    actors = models.ManyToManyField(Person, through='Role')

    def __str__(self):

        return '"{}" {}'.format(self.title, self.director)


class Role(models.Model):
    person_role = models.ForeignKey(Person)
    movie_role = models.ForeignKey(Movie)
    role = models.CharField(max_length=128)

    def __str__(self):
        return '{}, {}, {}'.format(self.person_role, self.movie_role, self.role)


