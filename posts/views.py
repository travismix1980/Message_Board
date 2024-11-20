#from django.shortcuts import render

# import our Post model
from django.views.generic import ListView
from .models import Post

# Create your views here.
# def post_list(request):
#     posts = Post.objects
#     return render(request, "post_list.html", {"posts": posts})

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'

