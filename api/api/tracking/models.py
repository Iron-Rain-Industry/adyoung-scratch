from django.db import models

# Create your models here.


class Workout(models.Model):
    workout = models.CharField(max_length=128)
    date = models.DateTimeField()

class Exercise(models.Model):
    exercise = models.CharField(max_length=128)    
    bodypart = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

class Set(models.Model):    
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    

    