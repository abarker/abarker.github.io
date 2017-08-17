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
# Some set SITEURL = 'http://localhost:8000' in this file and real one in publishconf.py.
SITEURL = 'https://abarker.github.io' # Doesn't seem to do much, needed for Disqus comments.
GITHUB_URL = 'https://github.com/abarker' # may not do anything; some themes make fork ribbon

DISQUS_SITENAME = 'abarker' # Should be the shortname.
##DISQUS_URL = 'https://abarker.disqus.com' # NOT USED FOR ELEGANT THEME, some themes use...
##DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY' # only for disqus_static plugin, may not need
##DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY' # only for disqus_static plugin, may not need

COMMENTS_INTRO = "Leave any comments below." # Appears before the comments at bottom.

PATH = 'content' # Directory for content, relative to main dir.

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
# Leave off now, since bugs.... docs say "Only set this to True when
# developing/testing and only if you fully understand the effect it can have on
# links/feeds."
RELATIVE_URLS = False

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

#DELETE_OUTPUT_DIRECTORY = True # This is set True in publishconf.py.

# =============================================================================
# =============================================================================
# Mostly my customizing below.
# =============================================================================
# =============================================================================

BASEPATH_alb = "/home/alb/programming/python/pelican_blog/"
THEMEPATH_alb = BASEPATH_alb + "pelican_themes/pelican-themes/"
PLUGINPATH_alb = BASEPATH_alb + "pelican-plugins/"
PLUGIN_PATHS = [PLUGINPATH_alb]
PLUGINS = []

LOAD_CONTENT_CACHE = False # Turn off caching; use if some mods not showing (esp. metadata)

# Ignore Vim swap files (patterns passed to glob).  Different setting in publishconf.py.
IGNORE_FILES = ["*.swp"]

# =============================================================================
# math stuff
# =============================================================================

# Plugin docs:
# https://github.com/getpelican/pelican-plugins/tree/master/render_math
PLUGINS.append("render_math")

#macros = ['/home/user/latex-macros.tex']
macros = []
#MATH_JAX = {'color': 'blue', 'align': 'left', 'macros': macros}
MATH_JAX = {'macros': macros,
            "color": "black",
            "align": "center",
            "indent": "0em", # Used if align is not "center"
            }


# =============================================================================
# section numbers
# =============================================================================

PLUGINS.append("section_number")
SECTION_NUMBER_MAX = 3

# =============================================================================
# theme stuff below
# =============================================================================

# TODO: This stuff was a kludge to switch back to default themes and try them out.
# Clean up, just use the cloned elegant theme.
use_copied_alb_version = False # Only set true if copy of dir has been made.

# =============================================================================
# Elegant theme (CURRENTLY USED)
# =============================================================================

# Example Elegant config file settings:
#    File: https://github.com/talha131/onCrashReboot/blob/master/pelicanconf.py
#    Appears as: http://oncrashreboot.com/

use_copied_alb_version = True
THEME = "cloned_pelican_elegant"

# Some recommended settings from the docs.
# http://oncrashreboot.com/elegant-best-pelican-theme-features#configuration-variables
# "Here are the variables that you should set in your configuration to get the
# most out of Elegant":

PLUGINS += ["sitemap"]
#PLUGINS += ["pelican_toc"] # Alternative to extract_tok below.
PLUGINS += ["extract_toc"]
PLUGINS += ["alb_tipue_search"] # For search, note copied dir since bugfix in the code.

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'search', '404']
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Setting below is needed with Elegant theme to get icons for email, GitHub, etc.,
# to display on article pages.
USE_SHORTCUT_ICONS=True

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

# NOTE below is for LANDING_PAGE_ABOUT dict, but I set the values separately
# first.  Use HTML in the text to get spaces, links, etc.
title = "Articles on various topics."
details = """

   I am a computer scientist with interests in machine learning, data analysis,
   mathematical logic systems, user interfaces for mathematics and data
   analysis, and quantum computing.  Computer science Ph.D. from UVA.

   <p>

   Available for hire; contact me by
   <a href="mailto:Allen.L.Barker@gmail.com" title="My email address" itemprop="email">
   email</a>.

   <p>

   I currently live in the Hampton Roads area of Virgina.

   """

LANDING_PAGE_ABOUT = { "title": title,
                       "details": details}

PROJECTS = [

             {"name": "pytest-helper",
              "url": "https://abarker.github.io/pytest-helper",
              "description": "Functions to help in using py.test (for example, easily"
                   " make modules self-testing when run as scripts)."
             },

             {"name": "set-package-attribute",
              "url": "https://abarker.github.io/set-package-attribute",
              "description": "Automatically set the __package__ attribute for a "
                  "Python module run as a script."

             },
             {"name": "Lyx Notebook",
              "url": "https://github.com/abarker/lyxNotebook",
              "description": "Use the Lyx word processor as a code-evaluating "
                   "notebook (similar to Mathematica notebooks or Jupyter notebooks)."
             },

             {"name": "pdfCropMargins",
              "url": "https://github.com/abarker/pdfCropMargins",
              "description": "A command-line utility to crop PDF files.  Like "
                   "the pdfcrop program on steroids."
             },

             {"name": "makeSpanningBackground",
              "url": "https://github.com/abarker/makeSpanningBackground",
              "description": "Make a background wallpaper from multiple images "
                   "to display them on multiple monitors."
             },

             {"name": "camel-snake-pep8",
              "url": "https://github.com/abarker/camel-snake-pep8",
              "description": "A tool that uses Rope to help safely refactor "
                   "Python projects to use PEP-8 naming conventions."
             },

           ]

# "These are the optional article meta data variables that you can use"
#
#     subtitle
#     summary
#     disqus_identifier
#     modified
#     keywords
#=======================================================================================


# =============================================================================
# Other themes.
# =============================================================================

# == Fresh theme ======================================================================
# Responsive HTML5, uses custom Google search, etc. Free license.
# Look into if get tired of Elegant (though the fonts, etc., would need mods).
# =====================================================================================
# https://github.com/jsliang/pelican-fresh/blob/master/README.md
# http://jsliang.com/pelican-fresh-demo/blog/
# Note the license is MIT but README says GPL, so might need to enquire.

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

