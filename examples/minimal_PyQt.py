#!/usr/bin/env python
# ##############################################################################
# # PROJ: PyQt                           AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: minimal_PyQt.py                                                      #
# # REPO: hoefkensj/PyQt.git                                                   #
# # HOST: github.com                                                           #
# # VERSION: 0.2.0                                                             #
# # UPDATED:  20230602                                                         #
# ##############################################################################
#
from sys import argv, exit
from PyQt import QtWidgets

QtApp   = QtWidgets.QApplication(argv)
wgt     = QtWidgets.QWidget()
lbl     = QtWidgets.QLabel()
layout  = QtWidgets.QVBoxLayout(wgt)
layout  = layout.addWidget(lbl)
#only here  to get name of the parentin the  line that follows
import PyQt ; lbl = lbl.setText(f'Using: {PyQt.__name__}')
wgt.show()
QtApp.exec()
