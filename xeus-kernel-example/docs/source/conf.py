# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys


project = "jupyterlite-sphinx-demo"
copyright = "2025, JupyterLite Contributors"
author = "JupyterLite Contributors"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "jupyterlite_sphinx",
    "sphinx_design",
    "myst_nb",
    "numpydoc",
]

# To be able to import example.py and disabled_examples/disabled_example.py here
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("disabled_examples"))

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for jupyterlite-sphinx ------------------------------------------

# A list of glob patterns relative to the source directory that match file
#  and directories to include as a part of the embedded JupyterLite site.
jupyterlite_contents = ["custom_contents/*"]

# Set this to False to unsilence the verbose output of the JupyterLite build
# process. This is useful for debugging.
jupyterlite_silence = True

# Strip out the JupyterLite contents from the output HTML files
strip_tagged_cells = True

# The global_enable_try_examples configuration option inserts the directives
# to all "Examples" processed by numpydoc or sphinx.ext.napoleon.
global_enable_try_examples = True

# The global_button_text configuration option sets the button text for all
# buttons, and can be overridden in individual TryExamples buttons as well.
try_examples_global_button_text = "Try it online"

# Considering the experimental nature of the TryExamples feature, this option
# allows setting a warning message to be displayed as a cell at the top of
# all interactive examples. This message can be written in Markdown.
try_examples_global_warning_text = (
    "This interactive example is experimental. Please report any issues "
    "you may find to the JupyterLite team via "
    "[the issue tracker](https://github.com/jupyterlite/sphinx-demo/issues/new). "
    "Thank you!"
)


# -- Options for MyST-NB -----------------------------------------------------

nb_execution_mode = "auto"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_logo = "_static/icon.svg"
html_static_path = ["_static"]
html_css_files = ["button_styling.css"]
html_js_files = ["pypi.js"]

# -- Options for the PyData Sphinx theme -------------------------------------

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/jupyterlite/sphinx-demo",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/jupyterlite-sphinx",
            "icon": "fa-custom fa-pypi",
            "type": "fontawesome",
        },
    ],
    "switcher": {
        "json_url": "https://jupyterlite.github.io/sphinx-demo/switcher.json",
        "version_match": "xeus",
    },
    "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "use_edit_page_button": True,
    "secondary_sidebar_items": {
        "**": ["page-toc", "sourcelink", "edit-this-page"],
        "index": ["page-toc"],
    },
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "jupyterlite",
    "github_repo": "sphinx-demo",
    "github_version": "main",
    "doc_path": "xeus-kernel-example/docs/source/",
}
