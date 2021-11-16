from django.contrib import admin

from .models import ArticlePost, User

#注册ArticlePost到admin中
admin.site.register(ArticlePost)
admin.site.register(User)
