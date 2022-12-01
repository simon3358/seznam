import django_filters
from django.db import models
from .models import Movie


class MovieFilter(django_filters.FilterSet):
    # set filtering fields, with 'contains' setting
    class Meta:
        model = Movie
        fields = ['name', 'source']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
