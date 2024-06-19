# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

project = 'Documentation'
copyright = '2023, Transferonline.'
html_title = 'Transfer Online Documentation'
author = 'D.Levsey'
release = '0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'rst2pdf.pdfbuilder',
    'sphinx.ext.todo',
    'sphinx_search.extension',
    'sphinx-prompt',
    'sphinx.builders.linkcheck',
    'sphinxcontrib.httpdomain',
    'hoverxref.extension',
    'sphinx_copybutton',
    'sphinx_togglebutton'
]

todo_include_todos = True

pdf_documents = [
    ('documents/solo/solo_approved/techstackguide/techstackguide_01',
     'techstackguide_01',
     'Tech Stack Guide',
     'TransferOnline',
     'manual'),
]


html_theme_options = {
    "repository_url": "https://github.com/levseyd01/ResourceHub",
    "use_source_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "source",
    "repository_branch": "stable",
    "use_repository_button": True,
    'prev_next_buttons_location': None,
    "use_issues_button": True,
    "collapse_navbar": False,
    "use_download_button": True
}

html_logo = "_static/sol0-logo.png"

html_theme = 'sphinx_book_theme'

templates_path = ['_templates']
exclude_patterns = ['_sources',
                    '_static']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

latex_elements = {
    'preamble': r'''
    \usepackage{lmodern}
    \renewcommand{\familydefault}{\sfdefault}
    ''',
}

