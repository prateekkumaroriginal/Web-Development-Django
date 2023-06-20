from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "all_posts"


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.related_post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

        context = {
            "post": post,
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)
