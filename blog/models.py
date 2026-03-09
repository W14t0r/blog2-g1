from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Published'
        DRAFT = 'DF', 'Draft'
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=200)
    publish= models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    t ="🥹"

    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts'
    )
    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]



    def __str__(self):
        return self.title

# Create your models here.
