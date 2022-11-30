from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Movie


class IndexView(generic.ListView):
    template_name = 'stream/index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.all()


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'stream/detail.html'
