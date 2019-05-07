# -*- coding: UTF-8 -*-
# author:yuliang

import sys
from PyQt4 import QtGui

from DeviceTest.DevMwnd import DevMwnd

QtGui.QApplication.setStyle("cleanlooks")
app = QtGui.QApplication( sys.argv )

if __name__ == '__main__':
    mainWnd = DevMwnd()
    mainWnd.show()
    app.exec_()