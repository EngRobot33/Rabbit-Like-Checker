from django.db import models


class Post(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class PostUser(models.Model):
    user_id = models.IntegerField(blank=True)
    post_id = models.IntegerField(unique=True, blank=True)

    def __str__(self):
        return f"User ID: {str(self.user_id)}, Post ID: {str(self.post_id)}"
