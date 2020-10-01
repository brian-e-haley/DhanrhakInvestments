from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(get_user_model(), models.CASCADE)

    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'pk': self.pk})

    def __repr__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    MULTIPLE_CHOICE = 'mc'
    SHORT_ANSWER = 'sa'
    CATEGORY_CHOICES = [(MULTIPLE_CHOICE, 'Multiple Choice'),
                        (SHORT_ANSWER, 'Short answer')]

    question = models.CharField(max_length=255)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    quiz = models.ForeignKey(Quiz, models.CASCADE, 'questions')

    def get_absolute_url(self):
        return reverse('home')  # TODO swap to question_detail once completed

    def __repr__(self):
        return str(self.question)

    def __str__(self):
        return str(self.question)


class Option(models.Model):
    text = models.CharField(max_length=255)
    correct = models.BooleanField()
    question = models.ForeignKey('Question', models.CASCADE, 'options')

    def get_absolute_url(self):
        return reverse('home')  # TODO swap to option_detail once completed

    def __repr__(self):
        return str(self.text)

    def __str__(self):
        return str(self.text)
