import re
import string
from time import mktime
from datetime import datetime
import feedparser
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model

from item.models import FeedItem


class FeedParser(object):

    def __init__(self, feed_source, model):
        app_name, model_name = model.split('.')
        self.model = get_model(app_name, model_name)
        self.valid_chars = "'-_.() %s%s" % (string.ascii_letters, string.digits)
        self.source = feed_source
        self.feed = feedparser.parse(self.source)

    def count(self):
        return len(self.feed.entries)

    def sync_feed_items(self):
        items = []

        for entry in self.feed.entries:
            if not self.does_item_exist(source_id=entry['id']):
                item = self.create_item_from_entry_dict(entry)
                item.save()
                items.append(item)
        return items

    def does_item_exist(self, source_id):
        try:
            self.model.objects.get(source_id=source_id)
            return True
        except ObjectDoesNotExist:
            return False

    def create_item_from_entry_dict(self, entry):
        item = self.model()
        item.source_url = entry['link']
        item.source_id = entry['id']
        item.source_title = ''.join(c for c in entry['title'] if c in self.valid_chars)
        item.thumbnail_url = entry['media_thumbnail'][0]['url']
        item.description = ''.join(c for c in entry['summary'] if c in self.valid_chars)
        item.author = None
        item.pub_date = None
        return item


class MultiFeedParser(object):

    def parse_feeds(self, feed_list):

        print "Starting to parse the feed list"

        for feed in feed_list:
            print "Parsing feed: %s" % feed
            parser = FeedParser(feed['url'], feed['model'])
            parser.sync_feed_items()

        print "Parsing finished"
