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
		return import_module(f"PyQt{v}")
	return f"PyQt{v}",load

def importSubMod(**mods):
	modname,load=ImportPyQt()
	# for fname in Path(module.__file__).parent.glob(f"Qt*.*"):
	for qt in [*iter_modules()]:
		if qt.name.startswith('Qt'):
			if (name:= getmodulename(qt.name)):
				mods[name] = import_module(f"{modname}.{name}")
				print(name)

	return mods

#Versions=detect()
PyQt= ImportPyQt()
Mods= importSubMod()