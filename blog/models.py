from django.db import models

class Post(models.Model):
    STATUS_CHOICES =(
        ('pub', 'Published'),#first one is for database second one is for display 
        ('drf', 'Draft'),
    )
    
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=3)
