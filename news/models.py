from django.db import models

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name


class Article(models.Model):
    title = models.CharField(max_length=200)
    article_text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
