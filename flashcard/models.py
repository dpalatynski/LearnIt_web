from django.db import models
from django import forms

# Create your models here.


class FlashcardCheckAnswer(models.Model):
    answer = models.CharField(max_length=200, default="", blank=True)
