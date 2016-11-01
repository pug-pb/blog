#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PUG-PB'
SITENAME = 'PUG-PB (Grupo de Usuários Python Paraíba)'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Recife'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Static files
STATIC_PATHS = ['images', 'pdfs']

# Blogroll
LINKS = (
    ('Fórum de Discussões', 'https://groups.google.com/forum/#!forum/pug-pb'),
    ('Grupo do Whattsapp', 'https://'),
         )

# Social widget
SOCIAL = (
    ('Facebook', 'https://facebook.com/pug-pb'),
    ('Twitter', 'https://twitter.com/pug-pb'),
    ('Email', 'mailto:pythonusergroup.pb@gmail.com')
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
