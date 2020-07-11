from django.db import models

# Create your models here.
class shorturl(models.Model):
    url = models.URLField(max_length = 220)
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.url
