from django.db import models

# Create your models here.
class Message(models.Model):

    CHOICES = (
        ('question', 'pytanie'),
        ('other', 'inne'),
    )
    email = models.EmailField()
    category = models.CharField(max_length=100, choices=CHOICES)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    fav_date = models.DateTimeField()
    fav_time = models.TextField()

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

