from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
