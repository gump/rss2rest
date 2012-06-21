from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from rss.parser import MultiFeedParser


class Command(BaseCommand):
    args = '<>'
    help = 'Syncs registered feeds'

    def handle(self, *args, **options):

        self.stdout.write('Beginning feed synchronisation')
        parser = MultiFeedParser()
        parser.parse_feeds(settings.RSS2REST_FEEDS)
        self.stdout.write('Synchronisation complete')

