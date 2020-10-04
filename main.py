#coding:utf-8

import sys
from sleepFaderDialog import *
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = SleepFaderDialogInstance()
	widget.show()
	app.exec_()