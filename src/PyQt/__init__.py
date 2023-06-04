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
from PyQt.main import ImportMod,importSubMod

modules['PyQt']=ImportMod()
for module in (mods:=importSubMod()):
	setattr(modules['PyQt'],module,mods[module])

# # globals()['PyQt']=PyQt
# for k in globals()['PyQt']:
# 	print(k)

