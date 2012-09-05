from django.conf.urls import patterns, include
from rss2rest.api import FeedItemResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


feed_item_resource = FeedItemResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rss2rest.views.home', name='home'),
    # url(r'^rss2rest/', include('rss2rest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(feed_item_resource.urls)),
)
