#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Hayato Nishi"
SITENAME = "Hayato Nishi | Personal Website"
# SITEURL = "https://hayato-n.github.io/WebPage"
SITEURL = ""

PATH = "content"

THEME = "./theme/Flex"

SITETITLE = AUTHOR
SITESUBTITLE = "Statistical Urban Analysis"
SITELOGO = SITEURL + "/images/Face.jpg"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "ja"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("UA", "http://ua.t.u-tokyo.ac.jp"), ("REIS", "https://shmzlab.jp/main"))

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Sorting pages
PAGES_SORT_ATTRIBUTE = "source_path"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
