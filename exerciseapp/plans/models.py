from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user= models.ForeignKey(User, related_name='user',on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    age=models.IntegerField()
    height=models.FloatField()
    weight=models.FloatField()
    workout_time=models.CharField(max_length=255,choices=[('once in a week', 'once in a week'), ('twice in a week', 'twice in a week'), ('daily', 'daily'),('rarely','rarely')])
    preferred_workout_time=models.CharField(max_length=255,choices=[ ('morning', 'morning'),('evening','evening')])
    
class DietPlan(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    
class ExercisePlan(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    
class Plans(models.Model):
    user_details=models.ForeignKey(UserDetails,related_name='user_detail',on_delete=models.CASCADE )
    name=models.TextField()
    description=models.TextField()
    diet_plan=models.ForeignKey(DietPlan, related_name='diet_plan',on_delete=models.DO_NOTHING)
    exercise_plan=models.ForeignKey(ExercisePlan,related_name='exercise_plan',on_delete=models.DO_NOTHING)