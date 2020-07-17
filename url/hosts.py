from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'url.hostsconf.urls', name='wildcard'),
    # host(r'blog', 'url.hostsconf.urls', name='blog'),
    host(r'live', ' settings.ROOT_URLCONF', name='live'),
)
