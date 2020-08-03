from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """ Home page of my blog website. """
    return render(request, 'blogs/index.html')

def posts(request):
    """ Page to show all posts in chronological order. """

    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """ Page to show an individual post. """
    post = BlogPost.objects.get(id=post_id)

    context = {'post': post}
    return render(request, 'blogs/post.html', context)

def new_post(request):
    """ Make a new post. """
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')
    
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """ Edit a existing post. """
    post = BlogPost.objects.get(id=post_id)
    title = post.title

    if request.method != 'POST':
        form = BlogForm(instance=post)
    else:
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post_id)
    
    context = {'post': post, 'title': title, 'form': form}
    return render(request, 'blogs/edit_post.html', context)