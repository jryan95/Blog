from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseForbidden

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


@login_required
def new_post(request):
    """ Make a new post. """
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')
    
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """ Edit a existing post. """
    post = BlogPost.objects.get(id=post_id)
    title = post.title

    check_topic_owner(request, post)

    if request.method != 'POST':
        form = BlogForm(instance=post)
    else:
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post_id)
    
    context = {'post': post, 'title': title, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    """ Deletes a post. """
    post = BlogPost.objects.get(id=post_id)

    if check_topic_owner(request, post):
        post.delete()

    context = {'post': post}
    return render(request, 'blogs/delete_post.html', context)

def check_topic_owner(request, post):
    if request.user.is_superuser:
        return True
    
    if request.user != post.owner:
        raise Http404
    else:
        return True