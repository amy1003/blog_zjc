from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '评论'
    def __str__(self):
        return self.text[:20]
