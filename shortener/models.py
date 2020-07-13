from django.db import models
from .utils import code_generator, create_shortcode

class shorturlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(shorturlManager, self).all(*args, **kwargs)
        qs =qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = shorturl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes +=1
        return "New code made: {i}".format(i=new_codes)

class shorturl(models.Model):
    url = models.URLField(max_length = 220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(shorturl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
