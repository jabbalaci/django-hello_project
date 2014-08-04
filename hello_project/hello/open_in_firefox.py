#!/usr/bin/env python

import os
import sys


def open_url(url, port):
    URL = "{url}:{port}".format(url=url, port=port)
    os.system('firefox -url "{url}" 2>/dev/null'.format(url=URL))


if __name__ == "__main__":
    port = "8000"
    if len(sys.argv) > 1:
        port = sys.argv[1]
    open_url("http://127.0.0.1", port)
