#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys

from unipath import Path

urls_py = """
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
)
""".strip()


def process(appname):
    appdir = Path(appname)
    if not appdir.isdir():
        print("Error: there is no app called {0}.".format(appdir))
        sys.exit(1)
    # else
    static = Path(appname, 'static', appname)
    static.mkdir(True)
    templates = Path(appname, 'templates', appname)
    templates.mkdir(True)
    urls = Path(appname, 'urls.py')
    if not urls.isfile():
        urls.write_file(urls_py)

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: {0} APP_NAME".format(sys.argv[0]))
        sys.exit(1)
    # else
    appname = sys.argv[1]
    process(appname)
