from django_cron import CronJobBase, Schedule
import requests
from .models import Movie


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 60
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'stream.my_cron_job'

    # save only new movies from API - for simplicity only a few attributes
    def do(self):
        API_URL = 'https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json'
        response = requests.get(API_URL)
        movies = response.json()

        for movie in movies:
            movie_exist = Movie.objects.filter(name=movie['name'])
            if movie_exist:
                continue
            movie_object = Movie(
                name = movie['name'],
                short_name = movie['shortName'],
                icon_uri = movie['iconUri'],
                manifest_uri = movie['manifestUri'],
                source = movie['source']
            )
            movie_object.save()
