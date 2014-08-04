#!/usr/bin/env python

import os
import sys


def graph(args):
    cmd = "python manage.py graph_models {apps} | dot -Tpng -o graph.png".format(apps=" ".join(args))
#    print cmd
    os.system(cmd)
    cmd = "eog graph.png"
#    print cmd
    os.system(cmd)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: {0} <app1> <app2> ...".format(sys.argv[0])
        sys.exit(0)
    #
    graph(sys.argv[1:])
