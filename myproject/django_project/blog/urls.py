from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView, CommentCreateView, CommentUpdateView, CommmentDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/new',
         CommentCreateView.as_view(), name='comment-create'),

    path('post/<int:pk1>/comment/<int:pk>/update/',
         CommentUpdateView.as_view(), name='comment-update'),

    path('post/<int:pk1>/comment/<int:pk>/delete/',
         CommmentDeleteView.as_view(), name='comment-delete'),

    path('about/', views.about, name='blog-about'),
]
