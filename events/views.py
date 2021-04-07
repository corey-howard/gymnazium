from django.shortcuts import render
from django.views import generic
from .models import Post

class events(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'events.html'

    def get(self, request):
        return render(request, 'events/events.html')

class events_detail(generic.DetailView):
    model = Post
    template_name = 'events_detail.html'

    def get(self, request):
        return render(request, 'events/events_detail.html')
