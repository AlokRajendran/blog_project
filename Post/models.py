from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey 

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    Author = models.ForeignKey(User, on_delete= models.CASCADE)
    Contents = models.TextField()
    Created_on = models.DateTimeField(auto_now_add=True)
    postcategory = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)

    class Meta:
        ordering = ["-Created_on"]

    def __str__(self):
        return self.title  
        
