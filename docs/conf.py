# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'Tic Tac Toe Package'  
copyright = '2024, Londera Han'  
author = 'Londera Han'        

# -- General configuration ---------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../tictactoe_zh2643')) 

extensions = [
    'sphinx.ext.autodoc',        
    'sphinx_autodoc_typehints',   
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'       
html_static_path = ['_static']
