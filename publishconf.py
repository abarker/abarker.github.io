#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *   # NOTE, we get all of pelicanconf.py unless overwritten.

#SITEURL = "https://abarker.github.io" # Use pelicanconf version.
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = 'abarker' # Use pelicanconf version.
#GOOGLE_ANALYTICS = ""

# =====================================
# Customizing below.
# =====================================

# Ignore Vim swap and content with DRAFT in it (patterns passed to Python glob).
IGNORE_FILES = ["*.swp", "*DRAFT*"]
#IGNORE_FILES = ["*.swp"]

