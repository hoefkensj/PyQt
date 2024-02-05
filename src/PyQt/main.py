#!/usr/bin/env python
# ##############################################################################
# # PROJ: PyQt                           AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: Qt.py                                                                #
# # REPO: hoefkensj/PyQt.git                                                   #
# # HOST: github.com                                                           #
# # VERSION: 0.2.0                                                             #
# # UPDATED:  20230602                                                         #
# ##############################################################################
#

from re import compile
from pathlib import Path
from inspect import getmodulename
from importlib import import_module
from pkgutil import iter_modules

# Regex Masks:
MASK_modv=r'(?P<MOD>{MOD})(?P<V>\d+)'
REX=compile(MASK_modv.format(MOD='PyQt'))

def detect_PyQt():
	v=[]
	for i in [*iter_modules()]:
		if ( QT := REX.match(i.name) ) :
			groups = QT.groupdict()
			v      += groups.get('V')
	return v

def ImportPyQt(*v):
	v = list(v) or detect_PyQt()
	if v is not None:
		v=v[-1]
	def load():
		module=import_module(f"PyQt{v}")
		module.__setattr__('version',v)
		return module
	return load()

def importSubMod(**mods):
	for qt in [*iter_modules()]:
		if qt.name.startswith('Qt'):
			if (name:= getmodulename(qt.name)):
				PyQt.__setattr__(name,import_module(f"PyQt{PyQt.version}.{name}"))
	return mods
	
#Versions=detect()
PyQt= ImportPyQt()
Mods= importSubMod()