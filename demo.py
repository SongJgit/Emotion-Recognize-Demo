
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import *

import Ui_level3
import os
from PySide6 import QtCore,QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
import argparse
from abc import abstractmethod
#import detect
#from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
#                                 QMediaPlayer)
#from PySide6.QtMultimediaWidgets import QVideoWidget
#from PySide6.QtMultimedia import QMediaPlayer,QMediaContent,QUrl
import detect

class ERDemo(object):
    def __init__(self):
        super().__init__()
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_level3.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        
        sys.stdout = EmittingStr()
        self.ui.view_edit.connect(sys.stdout, QtCore.SIGNAL("textWritten(QString)"), self.outputWritten)
        sys.stderr = EmittingStr()
        self.ui.view_edit.connect(sys.stderr, QtCore.SIGNAL("textWritten(QString)"), self.outputWritten)
        
        self.signal()
        MainWindow.show()
        sys.exit(app.exec())


    def signal(self):
        self.ui.file_btn.clicked.connect(self.chooseFileBt_click)
        self.ui.run_btn.clicked.connect(self.runBt_click)
        self.ui.play_btn.clicked.connect(self.play_click)
        return
    

    def chooseFileBt_click(self):
        #获取路径,需要选择的路径为待检测的wav目录，sentence的wav
        self.file_path= QFileDialog.getExistingDirectory(self.ui.centralwidget,"文件选择", os.getcwd())
        self.data=self.file_path.split('/')[-1] # 等待检测的wav名称
        self.avipath = os.path.join(os.getcwd(),'sess02\Session2\dialog\avi\DivX',self.data+".avi")
        
        if self.file_path == " ":
            return
        self.ui.data_edit.setText(self.file_path)
        
    
    def runBt_click(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('-gpu', type=str, default= '0',
                            help='gpu: default 0')
        parser.add_argument('-weights',type=str, default="snapshot",
                            help='where to load the models')
        parser.add_argument('-dataset',type=str, default='IEMOCAP')
        parser.add_argument('-data',type=str, default=self.data,help = 'data to detect')
        parser.add_argument('-inference',type=bool,default=True)
        args = parser.parse_args()
        print(args)
        detect.demo_main(args)
        
        return 0

    def play_click(self):
        #flag,img=self.cap.read()
        #self.view_edit.setPixmap(QPixmap.fromImage(img))
        #self.player = QMediaPlayer()
        #self.player.setVideoOutput(self.ui.view_widget)

        
        #print("cur_path = ", self.avipath)
        #self.player.setMedia(QMediaContent(QUrl(self.cur_path)))

        #self.player.play()
        return 0

    def outputWritten(self, text):
        cursor = self.ui.view_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.view_edit.setTextCursor(cursor)
        self.ui.view_edit.ensureCursorVisible()


class EmittingStr(QtCore.QObject):  
        textWritten = QtCore.Signal(str)  #定义一个发送str的信号
        def write(self, text):
            QApplication.processEvents()
            self.textWritten.emit(str(text))
            #sys.stderr.flush()


        @abstractmethod
        def flush(self) -> None:
            pass





if __name__ == '__main__':
    ERDemo()

