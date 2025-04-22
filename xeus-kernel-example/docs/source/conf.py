# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "jupyterlite-sphinx-demo"
copyright = "2025, JupyterLite Contributors"
author = "JupyterLite Contributors"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_nb", "jupyterlite_sphinx"]

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
}
