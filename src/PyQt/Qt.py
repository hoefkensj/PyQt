#!/usr/bin/env python
# ##############################################################################
# # PROJ: PyQt                           AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: Qt.py                                                                #
# # REPO: hoefkensj/PyQt.git                                                   #
# # HOST: github.com                                                           #
# # VERSION: 0.1.2                                                             #
# # UPDATED:  20230512                                                         #
# ##############################################################################
#
import re
from os import name
from re import compile,match
from pathlib import Path
from inspect import getmodulename
from importlib import import_module
from pkgutil import iter_modules

def detect(**versions):
	Modules=['PyQt','PySide']
	versions={mod : [] for mod in Modules}
	reStr='(?P<MOD>{MOD})(?P<V>\d+)'
	REXQT=compile(reStr.format(MOD=Modules[0]))
	REXSIDE=compile(reStr.format(MOD=Modules[1]))
	for installed in [*iter_modules()]:
		if (QT:=REXQT.match(installed.name)) or (SIDE:=REXSIDE.match(installed.name)):
			if QT:
				module=QT.groupdict()['MOD']
				version= QT.groupdict()['V']
			else:
				module=SIDE.groupdict()['MOD']
				version= SIDE.groupdict()['V']
			versions[module]+=[version]
	return versions

def ImportMod(*version,mod='PyQt'):
	global Versions
	if not version:
		if not Versions.get(mod):
			result=None
		else:
			result=import_module(f"{mod}{Versions.get(mod)[-1]}")
	else:
		if not Versions.get(mod) or version not in Versions.get(mod) :
			result=None
		else :
			result=import_module(f"{mod}{version}")
	return result



def importSubMod(mod):
	for filename in Path(PyQt.__file__).parent.glob(f"Qt*.*"):
		name = getmodulename(filename.name)
		if name:
			PyQt.__setattr__(name, import_module(f"{PyQt.__name__}.{name}"))
	return PyQt

Versions=detect()
PyQt=ImportMod(mod='PyQt')
PyQt = importSubMod(PyQt)
for attr in  dir(PyQt):
	if not attr.startswith('__'):
		print(attr,getattr(PyQt,attr) )
