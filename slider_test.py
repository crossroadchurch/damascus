import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from test_ui import Ui_MainWindow
from httpserver import DamascusServer
from UiElements import UiRegistry


class SliderTest(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ds = DamascusServer(self)
        UiRegistry.create()
        UiRegistry().addWindow(self)
        self.channel_sliders = [self.channel_1,
                                self.channel_2,
                                self.channel_3,
                                self.channel_4]
        self.channel_datas = [self.ch_data_1,
                              self.ch_data_2,
                              self.ch_data_3,
                              self.ch_data_4]
        self.channel_descs = [self.ch_desc_1,
                              self.ch_desc_2,
                              self.ch_desc_3,
                              self.ch_desc_4]
        return

    def closeEvent(self, event):
        self.deleteLater()
        self.ds.stop_server()
        return

    def adjustChannel(self, channel, data):
        self.channel_sliders[int(channel)-1].setValue(int(data))
        return

    def poll(self):
        channel_data = {'c001' : self.channel_sliders[0].value(),
                        'c002' : self.channel_sliders[1].value(),
                        'c003' : self.channel_sliders[2].value(),
                        'c004' : self.channel_sliders[3].value()}
        return channel_data


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = SliderTest()
    window.show()
    sys.exit(app.exec_())
