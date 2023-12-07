from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    topic= models.CharField(max_length=255)
    users= models.ManyToManyField(User, related_name='community')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-modified_at',)
    


class Message(models.Model):
    community= models.ForeignKey(Community,related_name='message',on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='message_user',on_delete=models.CASCADE)
    class Meta:
        ordering=('-modified_at',)
