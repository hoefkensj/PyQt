#!/usr/bin/env python
# ##############################################################################
# # PROJ: PyQt                           AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: __init__.py                                                          #
# # REPO: hoefkensj/PyQt.git                                                   #
# # HOST: github.com                                                           #
# # VERSION: 0.2.0                                                             #
# # UPDATED:  20230602                                                         #
# ##############################################################################
#

from sys import modules
from PyQt.main import ImportPyQt
from PyQt.lib import *
module=ImportPyQt()

modules['PyQt']=module #modules[Name]