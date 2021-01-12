from voltaire.pelican import *


SITENAME = u'Wonkypaedia'
PATH = './Wonkypaedia'


MENUITEMS_START = [
    ('Home', '/'),
    ('Search', '/search'),
]


PLUGINS += ['voltaire.search']
TEMPLATE_PAGES = {
    'search.html': 'search/index.html',
}


# PLUGINS += ['voltaire.search']
# TIPUE_SEARCH = True
# TEMPLATE_PAGES = {
#     'search.html': 'search/index.html',
# }
