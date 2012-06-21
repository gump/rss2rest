rss2rest
========

Turns RSS feeds into a RESTful API with the use of TastyPie and Feedparser

Installation
============

Install via PIP:

    $ pip install rss2rest


Add to your `INSTALLED_APPS` the following:

    INSTALLED_APPS = [
        ...,
        'tastypie',
        'rss2rest',
    ]

Define your feeds:

    RSS2REST_FEEDS = [
        {'feed': 'http://feedurl/',
         'model': 'rss2rest.FeedItem'},
    ]

Add RESTful routing to your `urls.py`:

    from rss2rest.api import FeedItemResource
    feed_item_resource = FeedItemResource()
    urlpatterns += patterns('rss2rest',
        (r'^api/', include(feed_item_resource.urls)),
    )

Usage
=====

Synchronise Feeds:

    ./manage.py syncrss2rest

Consume feeds go to:

    http://127.0.0.1/rss2rest/api/

Contribute
==========

Set up in development mode:

    $ git clone git://github.com/gump/rss2rest.git
    $ cd rss2rest
    $ mkvirtualenv rss2rest
    $ python setup.py develop
    $ cd sandbox/
    $ cp local_settings_sample.py local_settings.py
    $ ./manage.py syncdb
    $ ./manage.py test rss2rest

