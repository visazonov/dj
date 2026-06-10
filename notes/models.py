from django.db import models
from django.contrib.auth.models import User  # импортируем модель User


class Tag(models.Model):
    # id
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=9)  #       #aa000055


class Note(models.Model):
    # id
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="notes")
