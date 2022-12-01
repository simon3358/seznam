from django.urls import path
from . import views


app_name = 'stream'
urlpatterns = [
    path('', views.show_movies, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
