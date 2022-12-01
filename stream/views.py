from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Movie
from .filters import MovieFilter


def show_movies(request):
    movies = Movie.objects.all()
    filter = MovieFilter(request.GET, queryset=movies)
    context = {'filter': filter, 'movies': filter.qs}
    return render(request, 'stream/index.html', context)

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'stream/detail.html'
