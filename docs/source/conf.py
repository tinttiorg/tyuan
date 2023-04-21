# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Dr. T'
copyright = '2022, UniverSee'
author = 'Ting Yuan'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

master_doc = 'index'

root_doc = 'index'


# def supsub_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     node = docutils.nodes.superscript()
#     node2 = docutils.nodes.substitution_reference(refname=text)
#     node += [node2]
#     return [node],[]

# def setup(app):
#     app.add_role('supsub', supsub_role)