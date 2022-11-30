from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    iconUri = models.CharField(max_length=50)
    manifestUri = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    focus = models.BooleanField()
    disabled = models.BooleanField()
    extraText = models.JSONField()
    certificateUri = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    isFeatured = models.BooleanField()
    drm = models.JSONField()
    features = models.JSONField()
    licenseServers = models.JSONField()
    licenseRequestHeaders = models.JSONField()
    requestFilter = models.JSONField()
    responseFilter = models.JSONField()
    clearKeys = models.JSONField()
    extraConfig = models.JSONField()
    adTagUri = models.CharField(max_length=100)
    imaVideoId = models.CharField(max_length=50)
    imaAssetKey = models.CharField(max_length=50)
    imaContentSrcId = models.IntegerField()
    mimeType = models.CharField(max_length=50)
    mediaPlaylistFullMimeType = models.CharField(max_length=50)
    storedProgress = models.IntegerField()
    storedContent = models.JSONField()

    def __str__(self):
        return self.name
