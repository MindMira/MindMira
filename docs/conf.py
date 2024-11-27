# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# -- Path setup --------------------------------------------------------------

import os
import sys
# 프로젝트 루트 디렉토리와 'scr/' 디렉토리를 sys.path에 추가
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../scr'))


# -- Project information -----------------------------------------------------

project = 'MindMira'
copyright = '2024, MindMira Contributors'
author = 'MindMira Team'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'  # ReadTheDocs 기본 테마 사용

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for master document ---------------------------------------------

# The master toctree document.
master_doc = 'index'  # 루트 문서 파일 지정 (index.rst)


# -- Options for TODOs -------------------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
