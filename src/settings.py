#!/usr/bin/env python
# -*- coding: utf-8 -*-
AUTHOR = 'Zakiullah Khan Mohammed'
EMAIL = 'mail at khanio.com'
SITENAME = 'KhanIO'
#TAGLINE = 'does stuff the hard way'
SITEURL = 'http://www.khanio.com'
SITEURL_PUBLIC = 'http://www.khanio.com'
SITEURL_LOCAL = 'http://localhost:8000'
TIMEZONE = 'Asia/Singapore'
DEFAULT_LANG = 'en'
LOCALE = ''
DEFAULT_DATE_FORMAT = ('%b %d, %Y')

THEME="theme"
DEFAULT_CATEGORY = 'misc'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
RELATIVE_URLS = True
MARKUP = 'md'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/khan_io'),
          ('LinkedIn', 'https://linkedin.com/in/khanio'),
          ('Facebook', 'https://facebook.com/in/mkhanio'),
          ('Google +', 'https://plus.google.com/khanio'),
          ('GitHub', 'https://github.com/khanio'),)

DEFAULT_PAGINATION = 5

FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/category.%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'
FEED_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category.%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'

PAGE_DIR = ('pages/')
ARTICLE_DIR = ('posts/')

GOOGLE_ANALYTICS = 'UA-40023432-1'
DISQUS_SITENAME = 'khanio'
TWITTER_USERNAME = 'khan_io'
GITHUB_USERNAME = 'khanio'
GOOGLE_PLUS_LINK = ''
LINKEDIN_LINK = ''

REVERSE_ARCHIVE_ORDER = True
YEAR_ARCHIVE_SAVE_AS = True
MONTH_ARCHIVE_SAVE_AS = True
DAY_ARCHIVE_SAVE_AS = True
DISPLAY_PAGES_ON_MENU = False

FILES_TO_COPY = (
    ('extra/robots.txt', 'robots.txt'),
    ('extra/humans.txt', 'humans.txt'),
    ('extra/CNAME', 'CNAME'),
    ('extra/README.md', 'README.md'),
    ('extra/LICENSE.md', 'LICENSE.md'),
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/apple-touch-icon.png', 'apple-touch-icon.png'),
    ('extra/apple-touch-icon-precomposed.png', 'apple-touch-icon-precomposed.png'),
    ('extra/apple-touch-icon-57x57-precomposed.png', 'apple-touch-icon-57x57-precomposed.png'),
    ('extra/apple-touch-icon-72x72-precomposed.png', 'apple-touch-icon-72x72-precomposed.png'),
    ('extra/apple-touch-icon-114x114-precomposed.png', 'apple-touch-icon-114x114-precomposed.png'),
    ('extra/apple-touch-icon-144x144-precomposed.png', 'apple-touch-icon-144x144-precomposed.png'),
)

MENUITEMS = (
	('Home','index.html'),
	('Philosophy', 'pages/philosophy.html'),
	('Resume', 'pages/resume.html'),
	('Projects', 'pages/projects.html'),
	('Archive', 'archives.html'),
	('Contact Me', 'pages/contact-me.html'),
)

PLUGINS=['pelican.plugins.sitemap',]


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

