#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PUG-PB'
SITENAME = 'PUG-PB Blog'
SITEURL = 'http://pug-pb.github.io'

PATH = 'content'
THEME = "nest"
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
    ('Python', 'http://python.org'),
    ('Fórum PUG-PB', 'https://groups.google.com/forum/#!forum/pug-pb'),
         )

# Social widget
SOCIAL = (
    ('Fórum', 'https://groups.google.com/forum/#!forum/pug-pb'),
    ('Grupo do Telegram', 'https://'),
    ('Github', 'https://github.com/pug-pb'),
    ('Facebook', 'https://facebook.com/pug-pb'),
    ('Twitter', 'https://twitter.com/pug-pb'),
    ('Email', 'mailto:pythonusergroup.pb@gmail.com'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# NEST Template
SITESUBTITLE = 'Grupo de Usuários Python Paraiba'
# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [('Homepage', '/'),('Categorias','/categories.html')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = 'pug_banner.png'
NEST_HEADER_LOGO = '/images/pug_logo1.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = 'Mapa do Site'
NEST_SITEMAP_MENU = [('Arquivo', '/archives.html'),('Tags','/tags.html'), ('Autores','/authors.html')]
NEST_SITEMAP_ATOM_LINK = 'Atom Feed'
NEST_SITEMAP_RSS_LINK = 'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = 'Social'
NEST_LINKS_COLUMN_TITLE = 'Links'
# NEST_COPYRIGHT = u'&copy; blogname 2015'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = 'Homepage'
NEST_INDEX_HEADER_TITLE = ''
NEST_INDEX_HEADER_SUBTITLE = 'Grupo de Usuários Python Paraíba'
NEST_INDEX_CONTENT_TITLE = 'Postagens recentes'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = 'Arquivo'
NEST_ARCHIVES_HEAD_DESCRIPTION = 'Postagens Arquivadas'
NEST_ARCHIVES_HEADER_TITLE = 'Arquivo'
NEST_ARCHIVES_HEADER_SUBTITLE = 'Arquivo de todas as postagens'
NEST_ARCHIVES_CONTENT_TITLE = 'Arquivo'
# article.html
NEST_ARTICLE_HEADER_BY = 'Por'
NEST_ARTICLE_HEADER_MODIFIED = 'modificado'
NEST_ARTICLE_HEADER_IN = 'na categoria'
# author.html
NEST_AUTHOR_HEAD_TITLE = 'Posts por'
NEST_AUTHOR_HEAD_DESCRIPTION = 'Posts por'
NEST_AUTHOR_HEADER_SUBTITLE = 'Arquivo de Posts'
NEST_AUTHOR_CONTENT_TITLE = 'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = 'Lista de Autores'
NEST_AUTHORS_HEAD_DESCRIPTION = 'Lista de Autores'
NEST_AUTHORS_HEADER_TITLE = 'Lista de Autores'
NEST_AUTHORS_HEADER_SUBTITLE = 'Arquivos listados por autor'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = 'Categorias'
NEST_CATEGORIES_HEAD_DESCRIPTION = 'Arquivos listados por categoria'
NEST_CATEGORIES_HEADER_TITLE = 'Categorias'
NEST_CATEGORIES_HEADER_SUBTITLE = 'Arquivos listados por categoria'
# category.html
NEST_CATEGORY_HEAD_TITLE = 'Arquivo da Categora'
NEST_CATEGORY_HEAD_DESCRIPTION = 'Arquivo da Categora'
NEST_CATEGORY_HEADER_TITLE = 'Categoria'
NEST_CATEGORY_HEADER_SUBTITLE = 'Arquivo da Categora'
# pagination.html
NEST_PAGINATION_PREVIOUS = 'Anterior'
NEST_PAGINATION_NEXT = 'Próximo'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'
# Static files
# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/logo.svg': {'path': 'logo.svg'}
# }
