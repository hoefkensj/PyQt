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

def detect(*modules):
	#weird construction due to see ->                                             #TODO future: PySide?
	if not modules:
		modules=['PyQt',]
	REX=compile(MASK_modv.format(MOD=modules[0]))
	vers={mod : [] for mod in modules}

	for i in [*iter_modules()]:
		if ( QT := REX.match(i.name) ) :
			groups = QT.groupdict()
			mod    = groups.get('MOD')
			v      = groups.get('V')
			vers[mod] += [v]

	return vers

def ImportMod(*version,mod='PyQt'):
	V=detect()
	if not version:
		version=V[-1]
	else:
		version=max([i for i in version if i in V ])
	v = V.get(mod)
	if version:
		v=version
	if v is not None:
		v=v[-1]
		if v in V.get(mod):
			module=import_module(f"{mod}{v}")
			# modules[mod]=mod_loaded

	return module

def importSubMod(*module,**mods):
	if not module:
		module=[ImportMod(),]
	if module:
		module=module[0]
	for fname in Path(module.__file__).parent.glob(f"Qt*.*"):
		if (name:= getmodulename(fname.name)):
			mods[name] = import_module(f"{module.__name__}.{name}")
			print(name)
	return mods

#Versions=detect()
PyQt=ImportMod(mod='PyQt')
Mods= importSubMod(PyQt)


