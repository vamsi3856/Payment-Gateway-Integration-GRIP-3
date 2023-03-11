from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(max_length=30)
    post_date = models.DateField(auto_now=True)
    