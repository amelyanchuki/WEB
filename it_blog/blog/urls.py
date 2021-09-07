from django.urls import path
from blog.views import blog_page

urlpatterns = [
    path("", blog_page, name="blogs_page" ),
]

