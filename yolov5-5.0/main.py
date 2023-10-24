from login import *
from show import *
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys
import Qt_res_rc
import sys
import os
from PIL import Image

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import argparse
import time
from pathlib import Path
import shutil
import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi((self))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.win = InterfaceWindow()
        self.win.hide()
        self.ui.pushButton.clicked.connect(self._goto_inte)
        self.show()

    def _goto_inte(self):
        account=self.ui.lineEdit.text()
        password=self.ui.lineEdit_2.text()
        if account == "admin" and  password=="123456":
            self.win.show()
            self.close()
        else:
            pass

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


class InterfaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi((self))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_4.clicked.connect(self.getfile)
        self.ui.pushButton_6.clicked.connect(self.getfiles)
        self.ui.pushButton_8.clicked.connect(self.getVideo)
        self.ui.pushButton_5.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.show()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/maxsize.png"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon(u":/icons/icons/minimizeWhite.png"))

    def getVideo(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file',r'C:\Users\Administrator\Desktop\yolov5-5.0\data\images',"Image files (*.mp4)")
        print(self.fname)
        self.fname = self.fname.replace('\\', '/')
        str = (r'python detect3.py --source ' + self.fname)  # + '--exist-ok '
        os.system(str)

        path = os.listdir(r'runs\detect\exp')
        s = path[0]
        pathend = r'runs\detect\exp' + '\\' + s
        #I = Image.open(pathend)
        #I.show()

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(None, 'Open file',r'C:\Users\Administrator\Desktop\yolov5-5.0\data\images',"image files(*.jpg *.png)", None, QFileDialog.DontUseNativeDialog)
        #fname , _= QFileDialog.getOpenFileName(None, 'Open file', r'C:\Users\Administrator\Desktop\yolov5-5.0\data\images', "image files(*.jpg *.png)",None,QFileDialog.DontUseNativeDialog)
        #self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file',r'C:\Users\Administrator\Desktop\yolov5-5.0\data\images',"Image files (*.jpg *.gif)")
        #self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open file", ".", " Image files(*.jpg *.png)")
        #self.le.setPixmap(QPixmap(self.fname))
        print(fname)
        self._fname=fname.replace('\\','/')
        str = (r'python detect2.py --source '+self._fname) #+ '--exist-ok '
        os.system(str)

        path = os.listdir(r'runs\detect\exp')
        s = path[0]
        pathend = r'runs\detect\exp' + '\\' + s
        #I = Image.open(pathend)
        #I.show()

    def getfiles(self):
        str=(r'python detect.py ')
        os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
        os.system(str)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
