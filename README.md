example: 
```py
from sys import argv, exit
from Qt import PyQt

QtApp = PyQt.QtWidgets.QApplication(argv)
wgt = PyQt.QtWidgets.QWidget()
layout = PyQt.QtWidgets.QVBoxLayout(wgt)
lbl = PyQt.QtWidgets.QLabel()
lbl.setText(f'Using: {PyQt.__name__}')
layout.addWidget(lbl)
wgt.show()
exit(QtApp.exec())
```
