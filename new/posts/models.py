from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    #def __str__(self):
       # return self.title


class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    location = models.CharField(max_length=20)
