from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title+' | '+str(self.author)


class Comment(models.Model):
    viewer = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    def __str__(self):
        return self.post.title+' | '+str(self.viewer)

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers')

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='followings')



