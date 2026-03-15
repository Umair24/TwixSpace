from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="twix_likes", blank=True)

    
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
    def total_likes(self):
        return self.likes.count()

# after creating a model we have to register it into admin.py for displaying