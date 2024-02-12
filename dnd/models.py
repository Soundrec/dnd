# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class New(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    