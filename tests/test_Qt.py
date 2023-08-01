#!/usr/bin/env python
# ##############################################################################
# # PROJ: PyQt                           AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: test_Qt.py                                                           #
# # REPO: hoefkensj/PyQt.git                                                   #
# # HOST: github.com                                                           #
# # VERSION: 0.2.0                                                             #
# # UPDATED:  20230602                                                         #
# ##############################################################################
#
import unittest
from QDPrintTree import stdOut
from src import PyQt

class Tests(unittest.TestCase):
	def test_PyQt(self):
		Pyqt_Core=PyQt.PyQt.QtCore
		self.assertIsNotNone(PyQt.PyQt.QtCore)
		stdOut(PyQt=PyQt)
		return self


if __name__ == "__main__":
	unittest.main()