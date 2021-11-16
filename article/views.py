from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from article.models import ArticlePost


def article_list(request):
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)