from django.shortcuts import render
from django.views import generic
from .models import Movie
from .filters import MovieFilter


def show_movies(request):
    movies = Movie.objects.all()
    if request.method == 'GET' and 'order_field' in request.GET:
        sorting_field = request.GET['order_field']
        movies = movies.order_by(sorting_field)
    filter = MovieFilter(request.GET, queryset=movies)
    context = {'filter': filter, 'movies': filter.qs}
    return render(request, 'stream/index.html', context)

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'stream/detail.html'
