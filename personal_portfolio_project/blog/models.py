from django.db import models

class Blogs(models.Model):
    Created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
