from django.contrib.auth import get_user_model
from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(get_user_model(), models.CASCADE)

    def __repr__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)
