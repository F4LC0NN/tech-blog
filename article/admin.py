from django.contrib import admin
from article.models import Article, Author, Category

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)
