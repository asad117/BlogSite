from turtle import pos
from django.urls import reverse
from http.client import HTTPResponse
from pyexpat import model
from re import template
from statistics import mode
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from flask import request
from .models import Author, Post, Tag, Contact
from .form import ContactForm, CommentForm

# Create your views here.


class indexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):

        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]

#     return render(request, "blog/index.html", {"posts": latest_posts})


# def allPost(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-post.html", {"posts":all_posts})

class allPost(ListView):
    template_name = "blog/all-post.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[::-1]
        return data


# def postDetails(request, slug):
#     post_detail = get_object_or_404(Post, slug = slug)
#     return render(request, "blog/post-details.html",
#      {"post":post_detail,
#      "post_tags":post_detail.tags.all()
#      }
#      )

class PostDetails(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comment.all().order_by("-id")
        }
        return render(request, "blog/post-details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)

        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-details", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comment.all().order_by("-id")
        }
        return render(request, "blog/post-details.html", context)


def porfile(request, id):
    author_detail = Author.objects.get(id=id)
    return render(request, "blog/profile.html", {"author": author_detail})

# def PostData(request):
#     # form =PostForm()

#     # content = {"form":form}
#     # return render(request, "blog/blog-post.html", content)


def contactForm(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            user_mame = form.cleaned_data["user_name"]
            message = form.cleaned_data["message"]
            print(title)
            add_contact = Contact(
                title=title, user_name=user_mame, message=message)
            add_contact.save()
            return HttpResponseRedirect("")

    else:

        form = ContactForm()
        return render(request, "blog/blog-post.html", {"form": form})


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False

        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, "blog/stored-post.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)

            request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")
