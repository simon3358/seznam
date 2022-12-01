from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    icon_uri = models.CharField(max_length=50)
    manifest_uri = models.CharField(max_length=50)
    source = models.CharField(max_length=50)

    # focus = models.BooleanField()
    # disabled = models.BooleanField()
    # extra_text = models.JSONField()
    # certificate_uri = models.CharField(max_length=50)
    # description = models.CharField(max_length=50)
    # is_featured = models.BooleanField()
    # drm = models.JSONField()
    # features = models.JSONField()
    # license_servers = models.JSONField()
    # license_request_headers = models.JSONField()
    # request_filter = models.JSONField()
    # response_filter = models.JSONField()
    # clear_keys = models.JSONField()
    # extra_config = models.JSONField()
    # ad_tag_uri = models.CharField(max_length=100)
    # ima_video_id = models.CharField(max_length=50)
    # ima_asset_key = models.CharField(max_length=50)
    # ima_content_src_id = models.IntegerField()
    # mime_type = models.CharField(max_length=50)
    # media_playlist_full_mime_type = models.CharField(max_length=50)
    # stored_progress = models.IntegerField()
    # stored_content = models.JSONField()

    def __str__(self):
        return self.name



