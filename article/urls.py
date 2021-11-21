from django.urls import path
from . import views
app_name = 'article'

urlpatterns = [
    path('article_list/', views.article_list, name = 'article_list'),
    path('article_detail/<int:id>', views.article_detail, name = 'article_detail'),
    path('article_create/', views.article_create, name = 'article_create'),
    # 删除文章
    #path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path('article_safe_delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),

]