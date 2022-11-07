from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """Model representing a post category."""
    name = models.CharField(max_length=200, help_text='Enter a post category (e.g. Docker)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Post(models.Model):
    """Model representing a post."""
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 1000, help_text='Enter a brief description of the post')
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    category = models.ManyToManyField(Category, help_text = 'Select a category for this post')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this post."""
        return reverse('post-detail', args=[str(self.id)])


class Coment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.user.username