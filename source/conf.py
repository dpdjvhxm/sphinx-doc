# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from recommonmark.parser import CommonMarkParser
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AgensGraph Guide & Manual'
copyright = '2024, Bitnine Global'
author = 'Jaehoon, Lee'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []
language = 'en'

# -- Extensions configuration ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google Style Python Docstrings 사용 시 추가
    "recommonmark",
    "sphinx_multiversion",
]
add_module_names = False  # 문서에 클래스 및 함수를 표시할 때 경로 생략 시 추가

source_suffix = ['.rst', '.md']  # '.md' 파일을 포함하도록 설정

source_parsers = {
    '.md': CommonMarkParser,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = 'favicon.ico' # 파비콘
html_logo = 'bitnine_logo.png' # 로고

html_theme = 'sphinx_rtd_theme'



