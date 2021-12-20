"""GreenBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView, CategoryView, DateView, LikeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article"),
    path("add-post/", AddPostView.as_view(), name="add_post"),
    path("edit-post/<int:pk>/", UpdatePostView.as_view(), name="edit_post"),
    path("delete-post/<int:pk>/", DeletePostView.as_view(), name="delete_post"),
    path("article/<int:pk>/comment/", AddCommentView.as_view(), name="add_comment"),
    path("category/<str:category>/", CategoryView, name="category"),
    path('filtered-posts/<str:desc>/', DateView, name='filtered_posts'),
    path('like/<int:pk>', LikeView, name='like_post')
]
