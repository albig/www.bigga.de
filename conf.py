# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'www.bigga.de'
html_title = 'www.bigga.de'
copyright = '2022, Alexander Bigga'
author = 'Alexander Bigga'

language = 'de'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "ablog",
    "sphinx_panels",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*", "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/albig/",
  "twitter_url": "https://twitter.com/albigdd",
  "search_bar_text": "Seite durchsuchen...",
  "google_analytics_id": "",
  "navbar_end": ["search-field.html", "navbar-icon-links"],
  "show_toc_level": 2,
  "show_nav_level": 2,
  "footer_items": ["copyright", "sphinx-version", "datenschutz"]
}

html_favicon = "_static/favicon.ico"

html_logo = "_static/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_extra_path = ['_static/robots.txt']

# html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html", "sidebar-nav-bs.html"],
    "about": ["hello.html", "sidebar-nav-bs.html"],
    "blog": ['tagcloud.html', 'archives.html'],
    "blog/**": ['postcard.html', 'recentposts.html', 'archives.html'],
    "impressum/**": ["hello.html", "sidebar-nav-bs.html"]
}
blog_baseurl = "https://www.bigga.de/blog"
blog_title = "Alexander Bigga - Blog"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*/*/*"
blog_languages = {
    'de': ('Deutsch', None),
    'en': ('English', None),
    'fr': ('Francais', None),
}
blog_default_language = "de"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = [
    "deflist",
    "colon_fence",
]

# Bibliography and citations
# bibtex_bibfiles = ["_static/works.bib"]

# OpenGraph config
ogp_site_url = "https://www.bigga.de"
ogp_image = "https://www.bigga.de/_static/bigga-alexander.jpg"

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = "off"


extensions += ["sphinx_sitemap"]

html_baseurl = os.environ.get("SPHINX_HTML_BASE_URL", "http://127.0.0.1:8008/")
sitemap_locales = [None]
sitemap_url_scheme = "{link}"

rediraffe_redirects = {
}

def setup(app):
    app.add_css_file("custom.css")
