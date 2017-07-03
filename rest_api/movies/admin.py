from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
    # list_display = ("name")


@admin.register(Movie)
class PersonAdmin(admin.ModelAdmin):
    pass
    # list_display = ("title", "description", "director", "year", "actors")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
    # list_display = ("person_role", "movie_role", "role")


