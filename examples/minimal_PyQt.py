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
import PyQt
from PyQt import QtWidgets
QtApp   = QtWidgets.QApplication(argv)
wgt     = QtWidgets.QWidget()
layout  = QtWidgets.QVBoxLayout(wgt)

lbl     = QtWidgets.QLabel()
lbl.setText(f'Qt version: {PyQt.__name__}')
btn			=	QtWidgets.QPushButton()
btn.setText('Quit')
btn.clicked.connect(exit)
layout.addWidget(lbl)
layout.addWidget(btn)
wgt.show()
QtApp.exec()