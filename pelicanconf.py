#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""
Initially generated by the creator program, then customized.

For Pelican-specific settings, see
   http://docs.getpelican.com/en/3.6.3/settings.html

"""
from __future__ import unicode_literals

AUTHOR = 'Allen Barker'
SITENAME = "Allen Barker's Site"
SITEURL = 'https://abarker.github.io' # Doesn't seem to do much, at least with GitHub host.
#SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%m-%d-%Y'

DEFAULT_LANG = 'en'

# Slugs are the names for the web pages, such as abarker.github.io/<slug-string>
SLUGIFY_SOURCE = 'basename'  # Use file basenames for slugs if not specified.
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
JINJA_FILTERS = {}
TYPOGRIFY = True

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

# Social widgets
# The LHS string can be "Twitter", "Github", "GitTip", or "Email".
SOCIAL = (
        ('Github', 'http://github.com/abarker'),
#        ('GitTip', 'http://gittip.com/abarker'),
        ('Email', 'mailto:Allen.L.Barker@gmail.com'),
          )
SOCIAL_PROFILE_LABEL = 'Contact'
RELATED_POSTS_LABEL = 'Related Posts'
SHARE_POST_INTRO = 'Like this post? Share on:'

# URLs for pages, trailing slash to support HTTPS
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
# URLs for articles
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True # Useful when developing, turn off before uploading (to be safe).

# Sitemap plugin settings, for more options see
# https://github.com/getpelican/pelican-plugins/tree/master/sitemap
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

BASEPATH_alb = "/home/alb/programming/python/pelican_blog/"
THEMEPATH_alb = BASEPATH_alb + "pelican_themes/pelican-themes/"
PLUGINPATH_alb = BASEPATH_alb + "pelican-plugins/"
PLUGIN_PATHS = [PLUGINPATH_alb]
PLUGINS = []

# =============================================================================
# math stuff
# =============================================================================

PLUGINS.append("render_math")

#macros = ['/home/user/latex-macros.tex']
macros = []
#MATH_JAX = {'color': 'blue', 'align': 'left', 'macros': macros}
MATH_JAX = {'macros': macros}

# =============================================================================
# theme stuff below 
# =============================================================================

use_copied_alb_version = False # Only set true if copy of dir has been made.

#===== Elegant theme ===================================================================
# Top contender if customizable.  Many options listed on this page describing it here:
# Getting search to work:
# http://stackoverflow.com/questions/24187511/enable-search-function-in-pelican-powered-blog

use_copied_alb_version = True; THEME = "cloned_pelican_elegant"

# Some recommended settings from the docs.
# http://oncrashreboot.com/elegant-best-pelican-theme-features#configuration-variables
# "Here are the variables that you should set in your configuration to get the
# most out of Elegant":

PLUGINS.extend(["sitemap"])
#PLUGINS = ['sitemap', 'extract_toc', 'tipue_search'] # Use these when TOC set up...
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# 
# "These are the optional configuration variables that you can define"
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

# "These are the optional article meta data variables that you can use"
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

