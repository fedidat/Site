#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ben Fedidat'
SITENAME = "Ben's corner"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/fedidat'),
          ('github', 'https://github.com/fedidat')
          )

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites',
    'headerid']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

BOOTSTRAP_THEME = "darkly"

# THEME = "pelican-themes/pelican-blue-1.1"
# THEME = "pelican-themes/nice"
THEME = "pelican-themes/pelican-bootstrap3"

FAVICON = "favicon.png?"

#DISQUS_SITENAME = 'fedidat'
DISQUSURL = 'http://fedidat.com'

CC_LICENSE = True

STATIC_PATHS = [
    'images', 
    'extra'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.png': {'path': 'favicon.png'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README.md': {'path': 'README.md'}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
