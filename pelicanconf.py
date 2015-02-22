#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Thomas O'Donnell"
SITENAME = 'andytom.github.io'
SITEURL = 'https://andytom.github.io'
THEME = "../pure-single"

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

PROFILE_IMG_URL = 'https://avatars1.githubusercontent.com/u/108836?v=3&s=460'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('github', 'https://github.com/andytom/'),
)

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS = "UA-57520406-1"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
