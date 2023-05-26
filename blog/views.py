from django.shortcuts import render
from django.http import HttpResponse

def blog_post_list(request):
    # Logic to retrieve a list of blog posts from the database
    # You can customize this logic to fetch the posts you want to display

    # Example list of blog post titles
    posts = ['First Post', 'Second Post', 'Third Post']

    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

def blog_post_detail(request, post_id):
    # Logic to retrieve a specific blog post from the database
    # You can customize this logic to fetch the post based on the 'post_id'

    # Example blog post content
    post_content = f"Content of Blog Post {post_id}"

    context = {'post_content': post_content}
    return render(request, 'blog/post_detail.html', context)
