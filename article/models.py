from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    synopsis = models.TextField(max_length=500, null=True, blank=True)
    content = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'pk': self.pk})
