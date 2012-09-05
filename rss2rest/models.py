from abstract_models import *

class FeedItem(AbstractFeedItem):

    MAPPING = {
        'source_url': 'link',
        'source_id': 'id',
        'source_title': 'title',
        'source_description': 'summary',
    }

    class Meta:
        verbose_name = "Feed item"

class VimeoFeedItem(AbstractFeedItem):

    MAPPING = {
        'source_url': 'link',
        'source_id': 'id',
        'source_title': 'title',
        'source_description': 'summary',
    }

    class Meta:
        verbose_name = "Vimeo video"

class PictureFeedItem(AbstractFeedItem):

    class Meta:
        verbose_name = "Picture"

class FlickrFeedItem(PictureFeedItem):

    MAPPING = {
        'source_title': 'title',
        'source_description': 'media:description',
        'source_url': 'link',
        'source_author': 'media:credit',
        'source_author_url': 'author[flickr:profile]',
        'source_thumbnail_url': 'media:thumbnail[url]'
    }

    author_url = models.URLField(max_length=255)

    class Meta:
        verbose_name = "Flickr photo"
