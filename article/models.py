from django.db import models
# Django本身具有一个简单又完整的账号系统（User），足以满足一般网站的账号申请、建立、权限、群组等基本功能
# 因此这里导入内建的User模型，以便使用。
from django.contrib.auth.models import User

from django.utils import timezone

# 博客文章数据类型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    # 内部类 class Meta用于给model定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title



