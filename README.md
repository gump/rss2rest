rss2rest
========

Turns RSS feeds into a RESTful API with the use of TastyPie and Feedparser


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

