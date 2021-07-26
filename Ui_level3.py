# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'level3.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 880)
        MainWindow.setMaximumSize(QSize(16777215, 880))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.run_btn = QPushButton(self.centralwidget)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setMinimumSize(QSize(479, 40))

        self.horizontalLayout.addWidget(self.run_btn)

        self.play_btn = QPushButton(self.centralwidget)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMinimumSize(QSize(478, 40))

        self.horizontalLayout.addWidget(self.play_btn)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.data_edit = QTextEdit(self.centralwidget)
        self.data_edit.setObjectName(u"data_edit")
        self.data_edit.setMaximumSize(QSize(16777215, 40))
        self.data_edit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.data_edit, 1, 0, 1, 1)

        self.file_btn = QToolButton(self.centralwidget)
        self.file_btn.setObjectName(u"file_btn")
        self.file_btn.setMinimumSize(QSize(40, 40))
        self.file_btn.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_4.addWidget(self.file_btn, 1, 1, 1, 1)

        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        self.input_label.setFont(font)
        self.input_label.setLayoutDirection(Qt.LeftToRight)
        self.input_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.input_label, 0, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_4, 2, 1, 1, 1)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(36)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.view_edit = QTextBrowser(self.centralwidget)
        self.view_edit.setObjectName(u"view_edit")

        self.gridLayout_2.addWidget(self.view_edit, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 997, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"Run!", None))
        self.play_btn.setText(QCoreApplication.translate("MainWindow", u"Play\uff01", None))
        self.file_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Please select input data", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Emotion recognition", None))
    # retranslateUi

