# -- Imports -----------------------------------------------------------------

import datetime
import sphinx_bootstrap_theme
import os
import json


# -- Project information -----------------------------------------------------

v_e_r_s_i_o_n = 'version 99.99.99'
with open('version.json', 'r') as f_version:
    version_dict = json.load(f_version)
    v_e_r_s_i_o_n = version_dict['__version__']
project = 'Bid for Game'
copyright = f'{datetime.datetime.now().year}, Jeff Watkins. Version: {v_e_r_s_i_o_n}'
author = 'Jeff Watkins'


# -- General configuration ---------------------------------------------------

html_path = os.sep.join(['build', 'html', 'index.html'])
local_index_page = os.getcwd().replace('source', html_path)
print('-'*len(local_index_page))
print(local_index_page)
print('-'*len(local_index_page))

extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx_copybutton',
]

source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

numfig = True
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]
html_favicon = 'favicon.ico'
