from django.shortcuts import render
from django.urls import reverse_lazy

from . import urls

from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Create your views here.
from .models import Post


class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = [
        'title',
        'author',
        'body',
    ]
    success_url = reverse_lazy('blog: all')

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = [
        'title',
        'author',
        'body',
    ]
    success_url = reverse_lazy('blog: all')

class PostDeleteView(UpdateView):
    model = Post
    fields = [
        'title',
        'author',
        'body',
    ]
    success_url = reverse_lazy('blog: all')