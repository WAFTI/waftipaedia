from voltaire.pelican import *


SITENAME = u'Wonkypaedia'
PATH = './Wonkypaedia'
FILENAME_METADATA = '(?P<title>.*)'


MENUITEMS_START = [
    ('Home', '/'),
    ('Search', '/search'),
]


PLUGINS += ['voltaire.search']
TEMPLATE_PAGES = {
    'search.html': 'search/index.html',
}
