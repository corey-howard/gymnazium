from django.shortcuts import render
from django.views import generic
from .models import Post


def events(request):
    """ A view to return the events page """
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, "events/events.html", context)


def events_detail(request, slug):
    """ A view to return the events detail page """
    post = Post.objects.get(slug=slug)
    context = {'post': post}

    return render(request, "events/events_detail.html", context)
