from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(get_user_model(), models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile')  # TODO swap to the quiz_detail page later

    def __repr__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    body = models.CharField(max_length=255)
    category = models.
