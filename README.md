
Import PyQt, any version and use it and tits modules versionless
Currently Posix (Linux/MacOs) only srry
(as i dont have a working windows env atm)
tested on Linux(Gentoo) with python  3.9,3.10,3.11 and PyQt 5,6
untested on MacOs but should work

example: 
```py
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
```
