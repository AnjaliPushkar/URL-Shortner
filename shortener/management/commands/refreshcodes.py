from django.core.management.base import BaseCommand, CommandError
from shortener.models import shorturl

class Command(BaseCommand):
    help = 'Refreshes all Url shortcodes'

    def add_arguments(self, parser):
        parser.add_arguments('--items', type=int)

    def handle(self, *args, **options):
        return shorturl.objects.refresh_shortcodes(items=options['items'])
