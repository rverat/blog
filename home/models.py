from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=250, blank=True, null=True)
    instagram = models.CharField(max_length=250, blank=True, null=True)
    linkedin = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)


class Category(models.Model):
    """Model representing a post category."""
    name = models.CharField(max_length=200, help_text='Enter a post category (e.g. Docker)')

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this post."""
        return reverse('category-detail', args=[str(self.id)])


class Post(models.Model):
    """Model representing a post."""
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 1000, help_text='Enter a brief description of the post')
    image = models.ImageField(null = True)
    publish_date = models.DateTimeField(auto_now_add = True)
    slug=models.CharField(max_length=130)
    status = models.BooleanField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    category = models.ManyToManyField(Category, help_text = 'Select a category for this post')

    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')

    #def __str__(self):
     #   """String for representing the Model object."""
      #return self.title

    #def get_absolute_url(self):
     #   """Returns the URL to access a detail record for this post."""
      #  return reverse('post-detail', args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.author.username +  " Comment: " + self.content


class PostView(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """String for representing the Model object."""
        return self.author.username


class Like(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.author.username