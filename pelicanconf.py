#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DEEP-Hybrid-DataCloud Consortium'
SITENAME = u'DEEP Open Catalog'
SITEURL = 'https://marketplace.deep-hybrid-datacloud.eu'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ''


DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = "models/{slug}.html"
ARTICLE_SAVE_AS = 'models/{slug}.html'
ARCHIVES_SAVE_AS = "models/index.html"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["more_categories"]

THEME = "themes/deep"

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

MENUITEMS = (
    ("DEEP Open Catalog", "/"),
    ("Project page", "https://deep-hybrid-datacloud.eu/"),
    ("Docs", "https://docs.deep-hybrid-datacloud.eu/"),
)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
