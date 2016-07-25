#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Allen Barker'
SITENAME = 'Allen Barker'
SITEURL = 'https://abarker.github.io/'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
           ('GitHub Repos', 'https://github.com/abarker?tab=repositories'),
           ('GitHub Repos', 'https://github.com/abarker?tab=repositories'),
        )

# Social widget
SOCIAL = (
         ('You can add links in pelicanconf.py', '#'),
         ('You can add links in pelicanconf.py', '#'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ------------ alb modified theme selection stuff below 

use_copied_alb_version = False

BASEPATH_alb = "/home/alb/programming/python/pelican_blog/"
THEMEPATH_alb = BASEPATH_alb + "pelican_themes/pelican-themes/"
PLUGINPATH_alb = BASEPATH_alb + "pelican-plugins/"

#===== Elegant theme ===================================================================
# Top contender if customizable.  Many options listed on this page describing it here:
# http://oncrashreboot.com/elegant-best-pelican-theme-features
# Getting search to work:
# http://stackoverflow.com/questions/24187511/enable-search-function-in-pelican-powered-blog
use_copied_alb_version = True; THEME = "elegant"
# Here are the variables that you should set in your configuration to get the
# most out of Elegant

PLUGIN_PATHS = [PLUGINPATH_alb]
PLUGINS = ["sitemap", "render_math"]
# MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
# DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
# STATIC_PATHS = ['theme/images', 'images']
# TAG_SAVE_AS = ''
# CATEGORY_SAVE_AS = ''
# AUTHOR_SAVE_AS = ''
# 
# These are the optional configuration variables that you can define
# 
# RECENT_ARTICLES_COUNT (integer)  
RECENT_ARTICLES_COUNT = 30

# COMMENTS_INTRO ('string')
# SITE_LICENSE ('string')
# SITE_DESCRIPTION ('string')
SITE_DESCRIPTION = "Site description string."

# EMAIL_SUBSCRIPTION_LABEL ('string')
# EMAIL_FIELD_PLACEHOLDER ('string')
# SUBSCRIBE_BUTTON_TITLE ('string')
# MAILCHIMP_FORM_ACTION ('string')
# SITESUBTITLE ('string')

# LANDING_PAGE_ABOUT ({})
details = """
   I am a computer scientist.
   I have many interests.
   """
LANDING_PAGE_ABOUT = { "title": "Articles on various topics.",
                       "details": details}

# PROJECTS ([{},...])
PROJECTS = [
             {"name": "set-package-attribute",
              "url": "https://github.com/abarker/set-package-attribute",
              "description": "Automatically set the __package__ attribute for a "
              "Python module run as a script."
             }
           ]

# These are the optional article meta data variables that you can use
# 
#     subtitle
#     summary
#     disqus_identifier
#     modified
#     keywords
#=======================================================================================


# ==== Tuxlite ZF theme ================================================================
# Good for mobile, see its style.css for customization details.
#use_copied_alb_version = True; THEME = "tuxlite_zf"

# similar one, maybe better, haven't looked... doesn't seem to have customizable
# style.css file
#use_copied_alb_version = True; THEME = "tuxlite_tbs"
# ======================================================================================


# Doesn't look bad if customizable.  No mention of customizing, though.
#THEME = "bootstrap2"

# Not a bad look, if customizable.  Some vars described here:
# https://github.com/getpelican/pelican-themes/tree/master/gum
#THEME = "gum"

#THEME = "nice-blog" # THEME_COLOR = 'blue', can change
# https://github.com/guilherme-toti/nice-blog/tree/ceff20c3f38cd733649cb15618d6c0e85b62bfc6

#THEME = "new-bootstrap2" # not bad, but not fully done, see page title

#THEME = "backdrop" # FAILS without further tweaking, github version apparently newer
# while this one fails if fewer than three articles.
# Below line recommended for paginated sites on
#    https://github.com/getpelican/pelican-themes/tree/master/backdrop
#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

if use_copied_alb_version:
    THEMEPATH_alb += "../"
    THEME += "_alb"
THEME = THEMEPATH_alb + THEME
