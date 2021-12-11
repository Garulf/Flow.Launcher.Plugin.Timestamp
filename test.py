# -*- coding: utf-8 -*-
import sys
import os

plugindir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(plugindir)
sys.path.append(os.path.join(plugindir, "lib"))
sys.path.append(os.path.join(plugindir, "plugin"))

from pprint import pprint

from plugin import Main


if __name__ == '__main__':
    t = Main().query()
    pprint(t)
