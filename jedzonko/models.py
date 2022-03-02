from django.db import models
from enum import Enum
from datetime import date, datetime


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField()
    preparing = models.CharField(max_length=500, default="")

    class Meta:
        ordering = ['-votes','-created']


class Plan(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField(to=Recipe)

    class Meta:
        ordering = ['name', '-created']


class DayName(models.Model):
    class WeekDays(Enum):
        monday = ('Monday', 'Poniedziałek')
        tuesday = ('Tuesday', 'Wtorek')
        wednesday = ('Wednesday', 'Środa')
        thursday = ('Thursday', 'Czwartek')
        friday = ('Friday', 'Piątek')
        saturday = ('Saturday', 'Sobota')
        sunday = ('Sunday', 'Niedziela')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[1]

    name = models.CharField(max_length=32, choices=[x.value for x in WeekDays])
    order = models.IntegerField(unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=36)
    recipe = models.ManyToManyField(to=Recipe)
    plan = models.ManyToManyField(to=Plan)
    order = models.IntegerField(unique=True)
    day_name = models.ManyToManyField(to=DayName)



