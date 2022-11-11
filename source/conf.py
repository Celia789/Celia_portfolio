# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My_portfolio'
copyright = '2022, Celia Barat'
author = 'Celia Barat'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
  "github_url": "https://github.com/Celia789/",
  "icon_links": [
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/célia-barat-b32436204/",
            "icon": "fa-brands fa-linkedin",
        },        
        ],
  "search_bar_text": "Search this site...",
}