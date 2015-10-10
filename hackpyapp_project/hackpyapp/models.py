from django.db import models

# Create your models here.
class BodyPart(models.Model):
    name = models.CharField(max_length=255)

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    bodyPartTarget = models.ForeignKey(BodyPart)

class Training(models.Model):
    type = models.CharField(max_length=10)
    exerciseRelated = models.ForeignKey(Exercise)

class Routine(models.Model):
    name = models.CharField(max_length=255)

class DailyLog(models.Model):
    exercise_date = models.DateField
    routine = models.ForeignKey(Routine)


