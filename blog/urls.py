from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('<int:year>/<int:month>/<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
    # Add more URL patterns as needed
]
