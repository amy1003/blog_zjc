
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from blog.feeds import AllPostsRssFeed
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'mdeditor/',include('mdeditor.urls')),
    url(r'', include('comments.urls')),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
]
