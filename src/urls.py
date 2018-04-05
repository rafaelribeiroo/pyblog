from django.contrib import admin
from django.urls import path, include
from src.apps.blog import urls as blog_urls


app_name = 'principal'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blog_urls, namespace='blog')),
]
