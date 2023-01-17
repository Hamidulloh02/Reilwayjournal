from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Category(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.p
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = RichTextField()
    profile = models.ImageField(upload_to='images/', blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #
    # def __str__(self):
    #     return self.body
    #
    # def get_questions(self):
    #     body = list(self.raw_questions.all())
    #     random.shuffle(body )
    #     return body [:self.number_of_questions]

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
class Video(models.Model):
    video_title = models.CharField(max_length=500)
    video_link = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.video_title