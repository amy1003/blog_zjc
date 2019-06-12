from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mdeditor.fields import MDTextField   #必须导入
import markdown
from django.utils.html import strip_tags

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS= (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=20,verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS,verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS= (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=20, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS= (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
        (STATUS_DRAFT,'草稿')
    )

    title = models.CharField(max_length=255,verbose_name="标题")
    desc = models.CharField(max_length=1024,blank=True,verbose_name="摘要")
    # content = models.TextField(verbose_name="正文",help_text="正文必须markdown格式")
    content = MDTextField('content')  # 注意为MDTextField()
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    category = models.ForeignKey(Category,verbose_name="分类", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,verbose_name="标签")
    author = models.ForeignKey(User,verbose_name="作者", on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    views_num = models.PositiveIntegerField(default=0,verbose_name="浏览量")

    #统计阅读量
    def increase_views(self):
        self.views_num += 1
        self.save(update_fields=['views_num'])
    #自动生成摘要
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.desc:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.desc = strip_tags(md.convert(self.content))[:50]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-create_time']

