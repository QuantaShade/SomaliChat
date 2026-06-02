from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName 

class Content(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=255)
    postedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[::10] 

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="favorite")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user 

class Report:
    pass