from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import CommentForm
from .models import Post

# Create your views here.

def blog_list(request):

    posts = Post.objects.all()

    context = {
        'posts':posts
    }
    return render(request, 'blog/index.html', context)


def blog_details(request, slug):

    post = Post.objects.get(slug=slug)
  
    comments = post.comments.all()

    if request.method == 'POST':
        
        comment_form = CommentForm(request.post)

        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            # redirect to a new URL

            messages.success(request, 'Your comment submitted')
            return HttpResponseRedirect(request.path_info)



        # if a GET (or any other method) we will create a blank form
        else:

            comment_form = CommentForm()


        context = {
            'post':post,
            'comments':comments
        }

        return render(request, 'blog/details.html', context)
        






    

    
