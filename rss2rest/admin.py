from models import *
from django.contrib import admin


class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('source_title', 'source_pub_date', 'sync_date')

class FlickrFeedItemAdmin(FeedItemAdmin):
    pass

class PictureFeedItemAdmin(FeedItemAdmin):
    pass

class VimeoFeedItemAdmin(FeedItemAdmin):
    pass

admin.site.register(FeedItem, FeedItemAdmin)
admin.site.register(FlickrFeedItem, FlickrFeedItemAdmin)
admin.site.register(PictureFeedItem, PictureFeedItemAdmin)
admin.site.register(VimeoFeedItem, VimeoFeedItemAdmin)
