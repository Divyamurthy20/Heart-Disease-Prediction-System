from django.db import models

# Create your models here
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    phoneno = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class cardiac_arrest_prediction(models.Model):

    Fid= models.TextField()
    Age_In_Days= models.TextField()
    Sex= models.TextField()
    ChestPainType= models.TextField()
    RestingBP= models.TextField()
    RestingECG= models.TextField()
    MaxHR= models.TextField()
    ExerciseAngina= models.TextField()
    Oldpeak= models.TextField()
    ST_Slope= models.TextField()
    slp= models.TextField()
    caa= models.TextField()
    thall= models.TextField()
    Prediction= models.TextField()


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)