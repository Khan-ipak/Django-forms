from django.contrib.auth.models import User
from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    favorites = models.ManyToManyField(User, related_name="favorite_news", blank=True)  # Новое поле

    def __str__(self):
        return self.title
