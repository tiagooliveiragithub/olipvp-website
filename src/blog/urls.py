from django.urls import path
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', blog_views.PostDetailView.as_view(), name='post'),
    path('created_by/<int:author_pk>/', blog_views.CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>/', blog_views.CategoryListView.as_view(), name='category'),
    path('tag/<slug:slug>/', blog_views.TagListView.as_view(), name='tag'),
    path('search/', blog_views.SearchListView.as_view(), name='search'),
]