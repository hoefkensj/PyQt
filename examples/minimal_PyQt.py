#!/usr/bin/env python
# ##############################################################################
# # PROJ: PyQt                           AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: minimal_PyQt.py                                                      #
# # REPO: hoefkensj/PyQt.git                                                   #
# # HOST: github.com                                                           #
# # VERSION: 0.1.2                                                             #
# # UPDATED:  20230512                                                         #
# ##############################################################################
#
from sys import argv, exit
from PyQt import PyQt

QtApp = PyQt.QtWidgets.QApplication(argv)
wgt = PyQt.QtWidgets.QWidget()
layout = PyQt.QtWidgets.QVBoxLayout(wgt)
lbl = PyQt.QtWidgets.QLabel()
lbl.setText(f'Using: {PyQt.__name__}')
layout.addWidget(lbl)
wgt.show()
exit(QtApp.exec())