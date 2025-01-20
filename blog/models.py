from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=250)
    img_url=models.URLField(null=True)

    def __str__(self) :
          return self.title
