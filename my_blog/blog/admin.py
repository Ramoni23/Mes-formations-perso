from django.contrib import admin
from .models import Article, Category

# register your models here
admin.site.register(Article)
admin.site.register(Category)