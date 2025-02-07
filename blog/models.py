from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)  # Blog Title
    content = models.TextField()  # Blog Content

    def __str__(self):
        return self.title
