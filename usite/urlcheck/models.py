from django.db import models


class URL(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.URLField(max_length=200, unique=True,help_text="The URL to be monitored.")
    interval = models.DurationField(default='0:20:0')
    response_code = models.CharField(max_length=4, default=201)

