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


from pathlib import Path
from inspect import getmodulename
from importlib import import_module
from pkgutil import iter_modules


def detectQt():
	class linux:
		def __init__(slf):
			slf.dirs = ["usr"]
			slf.libs = ["lib", "lib32", "lib64"]
			# breakpoint()
			slf.dQt()
			# breakpoint()
			slf.dPyQt()

		def dQt(
			slf,
		):
			slf.Qt = []
			for folder in slf.dirs:
				for lib in slf.libs:
					for qt in Path(f"/{folder}/{lib}").glob("qt[0-9]*"):
						if qt.name.__str__()[2:].isnumeric():
							slf.Qt += [qt.name.__str__()[2:]]

		def dPyQt(slf):
			slf.PyQt = []
			for version in slf.Qt:
				for module in iter_modules():
					if module.name.casefold().startswith("pyqt"):
						candidate = module.name.removeprefix("PyQt")
						if candidate.isnumeric():
							slf.PyQt += [int(candidate)]

	return linux()


def importQt(version=None, modules=None):
	latest = detectQt().PyQt[-1]
	version = version or latest
	PyQt = import_module(f"PyQt{version}")
	return PyQt


def importPyQtModules(PyQt):
	for filename in Path(PyQt.__file__).parent.glob(f"Qt*.*"):
		name = getmodulename(filename.name)
		if name:
			PyQt.__setattr__(name, import_module(f"{PyQt.__name__}.{name}"))
	return PyQt


PyQt = importQt()
PyQt = importPyQtModules(PyQt)
