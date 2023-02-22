from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.TextField(max_length=100)
    last_name=models.TextField(max_length=100) 
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    phonenumber=models.IntegerField(null=True)
    

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    item=models.TextField(max_length=100)
    caption = models.TextField()
    price=models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    no_of_reports = models.IntegerField(default=0)
   

    def __str__(self):
        return self.user
    


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class ReportPost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.username   
    
class comments(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    comment=models.TextField()
    def __str__(self):
        return self.user

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    
class Product(models.Model):
    name= models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
    
