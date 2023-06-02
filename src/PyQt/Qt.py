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
from sys import modules
from re import compile
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
	module=None
	Versions=detect()
	v=Versions.get(mod)
	if version:
		v=version
	if v is not None:
		version=v[-1]
		if version in Versions[mod]:
			module=import_module(f"{mod}{version}")
			modules[mod]=module
	return module

def importSubMod(module,mod='PyQt'):
	for filename in Path(PyQt.__file__).parent.glob(f"Qt*.*"):
		name = getmodulename(filename.name)
		if name:
			submod=import_module(f"{PyQt.__name__}.{name}")
			module.__setattr__(name, submod)
			modules[name]=submod
	return module

Versions=detect()
PyQt=ImportMod(mod='PyQt')
PyQt = importSubMod(PyQt)


