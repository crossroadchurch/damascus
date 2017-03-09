# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(402, 411)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 281))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.channel_1 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.channel_1.setMaximum(255)
        self.channel_1.setPageStep(16)
        self.channel_1.setProperty("value", 0)
        self.channel_1.setSliderPosition(0)
        self.channel_1.setOrientation(QtCore.Qt.Vertical)
        self.channel_1.setTickPosition(QtGui.QSlider.TicksAbove)
        self.channel_1.setTickInterval(16)
        self.channel_1.setObjectName(_fromUtf8("channel_1"))
        self.horizontalLayout.addWidget(self.channel_1)
        self.channel_2 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.channel_2.setMaximum(255)
        self.channel_2.setPageStep(16)
        self.channel_2.setProperty("value", 0)
        self.channel_2.setOrientation(QtCore.Qt.Vertical)
        self.channel_2.setTickPosition(QtGui.QSlider.TicksAbove)
        self.channel_2.setTickInterval(16)
        self.channel_2.setObjectName(_fromUtf8("channel_2"))
        self.horizontalLayout.addWidget(self.channel_2)
        self.channel_3 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.channel_3.setMaximum(255)
        self.channel_3.setPageStep(16)
        self.channel_3.setProperty("value", 0)
        self.channel_3.setOrientation(QtCore.Qt.Vertical)
        self.channel_3.setTickPosition(QtGui.QSlider.TicksAbove)
        self.channel_3.setTickInterval(16)
        self.channel_3.setObjectName(_fromUtf8("channel_3"))
        self.horizontalLayout.addWidget(self.channel_3)
        self.channel_4 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.channel_4.setMaximum(255)
        self.channel_4.setPageStep(16)
        self.channel_4.setProperty("value", 0)
        self.channel_4.setOrientation(QtCore.Qt.Vertical)
        self.channel_4.setInvertedControls(False)
        self.channel_4.setTickPosition(QtGui.QSlider.TicksAbove)
        self.channel_4.setTickInterval(16)
        self.channel_4.setObjectName(_fromUtf8("channel_4"))
        self.horizontalLayout.addWidget(self.channel_4)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 310, 331, 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ch_data_1 = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ch_data_1.setObjectName(_fromUtf8("ch_data_1"))
        self.gridLayout.addWidget(self.ch_data_1, 0, 0, 1, 1)
        self.ch_data_2 = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ch_data_2.setObjectName(_fromUtf8("ch_data_2"))
        self.gridLayout.addWidget(self.ch_data_2, 0, 1, 1, 1)
        self.ch_data_3 = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ch_data_3.setObjectName(_fromUtf8("ch_data_3"))
        self.gridLayout.addWidget(self.ch_data_3, 0, 2, 1, 1)
        self.ch_data_4 = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ch_data_4.setObjectName(_fromUtf8("ch_data_4"))
        self.gridLayout.addWidget(self.ch_data_4, 0, 3, 1, 1)
        self.ch_desc_1 = QtGui.QLabel(self.gridLayoutWidget)
        self.ch_desc_1.setObjectName(_fromUtf8("ch_desc_1"))
        self.gridLayout.addWidget(self.ch_desc_1, 1, 0, 1, 1)
        self.ch_desc_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.ch_desc_2.setObjectName(_fromUtf8("ch_desc_2"))
        self.gridLayout.addWidget(self.ch_desc_2, 1, 1, 1, 1)
        self.ch_desc_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.ch_desc_3.setObjectName(_fromUtf8("ch_desc_3"))
        self.gridLayout.addWidget(self.ch_desc_3, 1, 2, 1, 1)
        self.ch_desc_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.ch_desc_4.setObjectName(_fromUtf8("ch_desc_4"))
        self.gridLayout.addWidget(self.ch_desc_4, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ch_desc_1.setText(_translate("MainWindow", "Channel 1", None))
        self.ch_desc_2.setText(_translate("MainWindow", "Channel 2", None))
        self.ch_desc_3.setText(_translate("MainWindow", "Channel 3", None))
        self.ch_desc_4.setText(_translate("MainWindow", "Channel 4", None))

