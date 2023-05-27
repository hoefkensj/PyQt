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

from pathlib import Path,os
from inspect import getmodulename
from importlib import import_module
from pkgutil import iter_modules

def OSParameters(OS):
	P={}
	P['posix']={}
	P['posix']['dirs']= ['usr',]
	P['posix']['arch']= ['','32','64']
	P['posix']['path']= ['/{DIR}/lib{ARCH}/']

	if P.get(OS):
		for dir in	P[OS]['dirs']:
			for arch in 	P[OS]['arch']:
				P[OS]['path']+=[
					P[OS]['path'][0].format(DIR=dir,ARCH=arch)
				]
	return P.get(OS)


def detectQt(P):
	def dQt():
		nonlocal d
		for path in P.get('path')[1:]:
			for qt in Path(path).glob("qt[0-9]*"):
				if qt.name.__str__()[2:].isnumeric():
					d['Qt'] += [qt.name.__str__()[2:]]

	def dPyQt():
		nonlocal d
		for module in iter_modules():
			if module.name.casefold().startswith("pyqt"):
					candidate = module.name.removeprefix("PyQt")
					if candidate.isnumeric():
							d['PyQt'] += [int(candidate)]

	d={'Qt': [], 'PyQt': [] }
	dQt()
	dPyQt()
	return d

def ImportPyQt(versions):
	vPyQt=versions['PyQt']
	def importPyQt(version=None, modules=None):
		latest = vPyQt[-1]
		version = version if version in vPyQt else latest
		PyQt = import_module(f"PyQt{version}")
		return PyQt
	return importPyQt


def importPyQtModules(PyQt):
	for filename in Path(PyQt.__file__).parent.glob(f"Qt*.*"):
		name = getmodulename(filename.name)
		if name:
			PyQt.__setattr__(name, import_module(f"{PyQt.__name__}.{name}"))
	return PyQt

OS=os.name
OSParams=OSParameters(OS)
Versions=detectQt(OSParams)
ImportPyQt=ImportPyQt(Versions)
PyQt = ImportPyQt()
PyQt = importPyQtModules(PyQt)
