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
    paginator = Paginator(posts,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts':posts,
        'page_obj':page_obj
    }
    return render(request, 'blog/index.html', context)


def blog_details(request, slug):

    post = Post.objects.get(slug=slug)
    similar_post = post.tags.similar_objects()[:4]
    comments = post.comments.all()

    if request.method == 'POST':
        
        comment_form = CommentForm(request.POST)

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
            'similar_post':similar_post,
            'comments':comments
        }

        return render(request, 'blog/details.html', context)
        






    

    
