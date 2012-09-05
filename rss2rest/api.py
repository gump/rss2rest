from tastypie.resources import ModelResource
from models import FeedItem, VimeoFeedItem, FlickrFeedItem


class FeedItemResource(ModelResource):
    class Meta:
        queryset = FeedItem.objects.filter(publish=True)
        resource_name = 'feed_item'

class FlickrItemResource(ModelResource):
    class Meta:
        queryset = FlickrFeedItem.objects.filter(publish=True)
        resource_name = 'flickr'

class VimeoItemResource(ModelResource):
    class Meta:
        queryset = VimeoFeedItem.objects.filter(publish=True)
        resource_name = 'vimeo'

