# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototyp.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import sys
from datetime import date
from threading import Thread
from threading import current_thread
from time import sleep

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import QRect
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTime

from abst.helper import get_data_from_key
from abst.helper import set_data_by_key


class Ui_MainWindow(object):
    inter = 0
    power = False
    alarm_off = False
    puls_ton = False
    farbe_ein = "white"
    farbe_aus = "grey"
    aed_active = False

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QRect(50, 10, 160, 463))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_l = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_l.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_l.setObjectName("verticalLayout_l")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_l.addWidget(self.label_5)
        self.TXT_HF = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.TXT_HF.setFont(font)
        self.TXT_HF.setAlignment(Qt.AlignCenter)
        self.TXT_HF.setWordWrap(False)
        self.TXT_HF.setObjectName("TXT_HF")
        self.verticalLayout_l.addWidget(self.TXT_HF, 0, Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_l.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_l.addWidget(self.label_4)
        self.TXT_NIBD_Sys = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.TXT_NIBD_Sys.setFont(font)
        self.TXT_NIBD_Sys.setAlignment(Qt.AlignCenter)
        self.TXT_NIBD_Sys.setWordWrap(False)
        self.TXT_NIBD_Sys.setObjectName("TXT_NIBD_Sys")
        self.verticalLayout_l.addWidget(
            self.TXT_NIBD_Sys, 0, Qt.AlignRight | Qt.AlignBottom)
        self.TXT_NIBD_Dia = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.TXT_NIBD_Dia.setFont(font)
        self.TXT_NIBD_Dia.setAlignment(Qt.AlignCenter)
        self.TXT_NIBD_Dia.setWordWrap(False)
        self.TXT_NIBD_Dia.setObjectName("TXT_NIBD_Dia")
        self.verticalLayout_l.addWidget(
            self.TXT_NIBD_Dia, 0, Qt.AlignRight | Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_l.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_l.addWidget(self.label_3)
        self.TXT_SpO2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.TXT_SpO2.setFont(font)
        self.TXT_SpO2.setAlignment(Qt.AlignCenter)
        self.TXT_SpO2.setWordWrap(False)
        self.TXT_SpO2.setObjectName("TXT_SpO2")
        self.verticalLayout_l.addWidget(
            self.TXT_SpO2, 0, Qt.AlignRight | Qt.AlignVCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(
            self.label, 0, Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_l.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.TXT_AF = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TXT_AF.setFont(font)
        self.TXT_AF.setAlignment(Qt.AlignCenter)
        self.TXT_AF.setWordWrap(False)
        self.TXT_AF.setObjectName("TXT_AF")
        self.horizontalLayout_4.addWidget(
            self.TXT_AF, 0, Qt.AlignHCenter)
        self.TXT_etCO2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.TXT_etCO2.setFont(font)
        self.TXT_etCO2.setAlignment(Qt.AlignCenter)
        self.TXT_etCO2.setWordWrap(False)
        self.TXT_etCO2.setObjectName("TXT_etCO2")
        self.horizontalLayout_4.addWidget(
            self.TXT_etCO2, 0, Qt.AlignRight)
        self.verticalLayout_l.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QRect(921, 3, 261, 451))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_r = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_r.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_r.setObjectName("verticalLayout_r")
        self.GROUP_L = QtWidgets.QVBoxLayout()
        self.GROUP_L.setObjectName("GROUP_L")
        self.BTN_AED = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_AED.setObjectName("BTN_AED")
        self.GROUP_L.addWidget(self.BTN_AED)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tBTN_Energie_w = QtWidgets.QToolButton(
            self.verticalLayoutWidget_4)
        self.tBTN_Energie_w.setObjectName("tBTN_Energie_w")
        self.horizontalLayout_3.addWidget(self.tBTN_Energie_w)
        self.TXT_Energie = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TXT_Energie.setFont(font)
        self.TXT_Energie.setText("200")
        self.TXT_Energie.setAlignment(Qt.AlignCenter)
        self.TXT_Energie.setObjectName("TXT_Energie")
        self.horizontalLayout_3.addWidget(self.TXT_Energie)
        self.tBTN_Energie_m = QtWidgets.QToolButton(
            self.verticalLayoutWidget_4)
        self.tBTN_Energie_m.setObjectName("tBTN_Energie_m")
        self.horizontalLayout_3.addWidget(self.tBTN_Energie_m)
        self.GROUP_L.addLayout(self.horizontalLayout_3)
        self.BTN_Laden = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_Laden.setObjectName("BTN_Laden")
        self.GROUP_L.addWidget(self.BTN_Laden)
        self.BTN_Schock = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.BTN_Schock.setFont(font)
        self.BTN_Schock.setObjectName("BTN_Schock")
        self.GROUP_L.addWidget(self.BTN_Schock)
        self.verticalLayout_r.addLayout(self.GROUP_L)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_r.addItem(spacerItem2)
        self.GROUP_R = QtWidgets.QVBoxLayout()
        self.GROUP_R.setObjectName("GROUP_R")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BTN_NIBD = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_NIBD.setCheckable(False)
        self.BTN_NIBD.setObjectName("BTN_NIBD")
        self.horizontalLayout.addWidget(self.BTN_NIBD)
        self.BTN_INT = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_INT.setAutoDefault(False)
        self.BTN_INT.setObjectName("BTN_INT")
        self.horizontalLayout.addWidget(self.BTN_INT)
        self.GROUP_R.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BTN_12K = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_12K.setAutoFillBackground(False)
        self.BTN_12K.setObjectName("BTN_12K")
        self.horizontalLayout_2.addWidget(self.BTN_12K)
        self.BTN_ABLT = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_ABLT.setObjectName("BTN_ABLT")
        self.horizontalLayout_2.addWidget(self.BTN_ABLT)
        self.GROUP_R.addLayout(self.horizontalLayout_2)
        self.BTN_EKG_TON = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_EKG_TON.setObjectName("BTN_EKG_TON")
        self.GROUP_R.addWidget(self.BTN_EKG_TON)
        self.BTN_ALARM = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.BTN_ALARM.setObjectName("BTN_ALARM")
        self.GROUP_R.addWidget(self.BTN_ALARM)
        self.verticalLayout_r.addLayout(self.GROUP_R)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(
            QRect(49, 460, 1131, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_bottom = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_5)
        self.horizontalLayout_bottom.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_bottom.setObjectName("horizontalLayout_bottom")
        self.BTN_Power = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.BTN_Power.setObjectName("BTN_Power")
        self.horizontalLayout_bottom.addWidget(self.BTN_Power)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_bottom.addItem(spacerItem3)
        self.TXT_Date = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.TXT_Date.setAlignment(Qt.AlignCenter)
        self.TXT_Date.setObjectName("TXT_Date")
        self.horizontalLayout_bottom.addWidget(self.TXT_Date)
        self.TXT_Time = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.TXT_Time.setMinimumSize(QSize(76, 78))
        self.TXT_Time.setAlignment(Qt.AlignCenter)
        self.TXT_Time.setObjectName("TXT_Time")
        self.horizontalLayout_bottom.addWidget(
            self.TXT_Time, 0, Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_bottom.addItem(spacerItem4)
        self.BTN_Credits = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.BTN_Credits.setObjectName("BTN_Credits")
        self.horizontalLayout_bottom.addWidget(self.BTN_Credits)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(
            QRect(230, 10, 661, 441))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_m = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_5)
        self.verticalLayout_m.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_m.setObjectName("verticalLayout_m")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_m.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_m.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_m.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "HF bpm"))
        self.TXT_HF.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "NIBD mmHg"))
        self.TXT_NIBD_Sys.setText(_translate("MainWindow", "---"))
        self.TXT_NIBD_Dia.setText(_translate("MainWindow", "---"))
        self.label_3.setText(_translate("MainWindow", "SpO2 %"))
        self.TXT_SpO2.setText(_translate("MainWindow", "--"))
        self.label.setText(_translate("MainWindow", "AF"))
        self.label_2.setText(_translate("MainWindow", "etCO2 mmHg"))
        self.TXT_AF.setText(_translate("MainWindow", "--"))
        self.TXT_etCO2.setText(_translate("MainWindow", "--"))
        self.BTN_AED.setText(_translate("MainWindow", "AED"))
        self.tBTN_Energie_w.setText(_translate("MainWindow", "<"))
        self.tBTN_Energie_m.setText(_translate("MainWindow", ">"))
        self.BTN_Laden.setText(_translate("MainWindow", "Laden"))
        self.BTN_Schock.setText(_translate("MainWindow", "SCHOCK"))
        self.BTN_NIBD.setText(_translate("MainWindow", "NIBD"))
        self.BTN_INT.setText(_translate("MainWindow", "INT"))
        self.BTN_12K.setText(_translate("MainWindow", "12-K"))
        self.BTN_ABLT.setText(_translate("MainWindow", "ABLT"))
        self.BTN_EKG_TON.setText(_translate("MainWindow", "EKG"))
        self.BTN_ALARM.setText(_translate("MainWindow", "Alarm"))
        self.BTN_Power.setText(_translate("MainWindow", "Power"))
        self.TXT_Date.setText(_translate("MainWindow", "02.12.2022"))
        self.TXT_Time.setText(_translate("MainWindow", "00:00"))
        self.BTN_Credits.setText(_translate("MainWindow", "About"))

        self.BTN_Power.setStyleSheet(f'background-color: {self.farbe_ein}')
        self.BTN_EKG_TON.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_AED.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.tBTN_Energie_w.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.tBTN_Energie_m.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_Laden.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_Schock.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_NIBD.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_INT.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_12K.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_ABLT.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_ALARM.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_Credits.setStyleSheet(f"background-color: {self.farbe_aus}")

        self.BTN_Schock.setEnabled(False)

        self.BTN_AED.clicked.connect(self.BTN_AED_clicked)
        self.tBTN_Energie_w.clicked.connect(self.tBTN_Energie_w_clicked)
        self.tBTN_Energie_m.clicked.connect(self.tBTN_Energie_m_clicked)
        self.BTN_Laden.clicked.connect(self.BTN_Laden_clicked)
        self.BTN_Schock.clicked.connect(self.BTN_Schock_clicked)
        self.BTN_NIBD.clicked.connect(self.BTN_NIBD_clicked)
        self.BTN_INT.clicked.connect(self.BTN_INT_clicked)
        self.BTN_12K.clicked.connect(self.BTN_12K_clicked)
        self.BTN_ABLT.clicked.connect(self.BTN_ABLT_clicked)
        self.BTN_EKG_TON.clicked.connect(self.BTN_EKG_TON_clicked)
        self.BTN_ALARM.clicked.connect(self.BTN_ALARM_clicked)
        self.BTN_Power.clicked.connect(self.BTN_Power_clicked)
        self.BTN_Credits.clicked.connect(self.BTN_Credits_clicked)

    def reset(self) -> None:
        # Umfärben
        self.BTN_Power.setStyleSheet(f'background-color: {self.farbe_ein}')
        self.BTN_EKG_TON.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_AED.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.tBTN_Energie_w.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.tBTN_Energie_m.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_Laden.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_Schock.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_NIBD.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_INT.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_12K.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_ABLT.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_ALARM.setStyleSheet(f"background-color: {self.farbe_aus}")
        self.BTN_Credits.setStyleSheet(f"background-color: {self.farbe_aus}")
        # Text zurücksetzten
        self.TXT_HF.setText("--")
        self.TXT_NIBD_Sys.setText("---")
        self.TXT_NIBD_Dia.setText("---")
        self.TXT_SpO2.setText("--")
        self.TXT_AF.setText("--")
        self.TXT_etCO2.setText("--")

    def einschalten(self) -> None:
        self.BTN_EKG_TON.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_AED.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.tBTN_Energie_w.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.tBTN_Energie_m.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_Laden.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_Schock.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_NIBD.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_INT.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_12K.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_ABLT.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_ALARM.setStyleSheet(f"background-color: {self.farbe_ein}")
        self.BTN_Credits.setStyleSheet(f"background-color: {self.farbe_ein}")
        # Umfärben des Power Button
        self.BTN_Power.setStyleSheet("background-color: green")
        # Starten der Uhr
        thread_time = Thread(target=self.show_time)
        thread_time.start()
        # Aktuallisieren des Datum
        current_date = date.today().strftime('%d.%m.%y')
        self.TXT_Date.setText(current_date)

    def show_time(self) -> None:
        while True:
            q_current_time = QTime.currentTime()
            current_time = q_current_time.toString('hh:mm:ss')
            self.TXT_Time.setText(current_time)
            if not self.power:
                self.TXT_Time.setText('00:00:00')
                sys.exit(1)

    def BTN_Power_clicked(self) -> None:
        print("DEBUG: POWER pushed")
        if self.power:
            self.power = False
            self.reset()

        else:
            self.power = True
            self.einschalten()

    def aed_work(self) -> None:
        while self.aed_active:
            if bool(get_data_from_key("patches")):
                print("Analyse, CPR unterbrechen")
                sleep(5)
                if bool(get_data_from_key("schockbar")):
                    print("Schock empfohlen")
                    #Todo Handle erfolgreicher Schock
                else:
                    print("Kein Schock empfohlen")
                sleep(10)
            else:
                print("Elektroden Überprüfen")
                sleep(10)
                self.aed_work()
        sys.exit(1)

    def BTN_AED_clicked(self) -> None:
        print("DEBUG: AED pushed")
        if not self.aed_active:
            self.aed_active = True
            self.BTN_AED.setStyleSheet('background-color: green')
            print("Elektroden kleben")  # TODO Audio
            print("Mit cpr beginnen")
            thread_aed = Thread(target=self.aed_work)
            thread_aed.start()
        else:
            self.aed_active = False
            self.BTN_AED.setStyleSheet(f'background-color: {self.farbe_ein}')

    def tBTN_Energie_w_clicked(self) -> None:
        print("DEBUG: ENERGIE_W pushed")
        energie = int(self.TXT_Energie.text())
        if energie - 25 <= 0:
            pass
        else:
            energie -= 25
            set_data_by_key("energie", energie)
            self.TXT_Energie.setText(str(energie))

    def tBTN_Energie_m_clicked(self) -> None:
        print("DEBUG: ENERGIE_M pushed")
        energie = int(self.TXT_Energie.text())
        if energie + 25 > 400:
            pass
        else:
            energie += 25
            set_data_by_key("energie", energie)
            self.TXT_Energie.setText(str(energie))

    def BTN_Laden_clicked(self) -> None:
        print("DEBUG: LADEN pushed")
        # Aktiveren des Schockbuttton
        self.BTN_Schock.setEnabled(True)

    def BTN_Schock_clicked(self) -> None:
        print("DEBUG: SCHOCK pushed")

    def BTN_NIBD_clicked(self) -> None:
        print("DEBUG: NIBD pushed")
        thread_nibd = Thread(target=self.get_data_nibd)
        thread_nibd.start()

    def get_data_nibd(self) -> None:
        # Farbe zu gelb
        self.BTN_NIBD.setStyleSheet('background-color: yellow')
        # Sound abspielen und warten
        self.nibd_sound_and_wait()
        # get Data
        syst = get_data_from_key("systole")
        dias = get_data_from_key("diastole")
        # set Text
        self.TXT_NIBD_Sys.setText(str(syst))
        self.TXT_NIBD_Dia.setText(str(dias))
        # Farbe zu Grün
        self.BTN_NIBD.setStyleSheet(f'background-color: {self.farbe_ein}')
        # Thread beenden
        sys.exit(1)

    def nibd_sound_and_wait(self) -> None:
        # Todo play Sound
        # Todo anpassen des warte intervalls
        sleep(5)

    def BTN_INT_clicked(self) -> None:
        print("DEBUG: INT pushed")
        # set intervall
        if self.inter == 0:
            thread_int = Thread(target=self.helerp_int)
            thread_int.start()

        if self.inter == 0:
            self.inter = 2
            self.BTN_INT.setText(str(self.inter) + " min")
        elif self.inter == 2:
            self.inter = 5
            self.BTN_INT.setText(str(self.inter) + " min")
        elif self.inter == 5:
            self.inter = 10
            self.BTN_INT.setText(str(self.inter) + " min")
        elif self.inter == 10:
            self.inter = 15
            self.BTN_INT.setText(str(self.inter) + " min")
        else:
            self.inter = 0
            self.BTN_INT.setText("INT")

    def helerp_int(self) -> None:
        sleep(10)
        while True:
            temp_inter = self.inter
            sleep(temp_inter * 60)
            if self.inter == 0:
                break
            elif self.inter == temp_inter:
                self.BTN_NIBD_clicked()
            else:
                sleep(self.inter - temp_inter)
                print("Hie")
        sys.exit(1)

    def BTN_12K_clicked(self) -> None:
        print("DEBUG: 12K pushed")

    def BTN_ABLT_clicked(self) -> None:
        print("DEBUG: ABLT pushed")

    def ekg_ton_work(self) -> None:
        # Todo play Sound in Rythmus von ekg Kurve -> bei jedem "Maximum" ein Ton
        # Todo je höher hf desto höher auch ton
        print('DEBUG: Sound ON')
        while True:
            if not self.puls_ton:
                print('DEBUG: Sound OFF')
                sys.exit(1)

    def BTN_EKG_TON_clicked(self) -> None:
        print("DEBUG: EKG_TON pushed")
        if self.puls_ton is True:
            self.puls_ton = False
            self.BTN_EKG_TON.setStyleSheet("background-color: white")
        else:
            self.puls_ton = True
            # starten des workers
            thread_ekg_ton = Thread(target=self.ekg_ton_work)
            thread_ekg_ton.start()
            # Frabe zu Grün
            self.BTN_EKG_TON.setStyleSheet("background-color: green")

    def alarm_work(self) -> None:
        # Btn ausschalten
        self.BTN_ALARM.setEnabled(False)
        self.BTN_ALARM.setStyleSheet('background-color: yellow')
        # set global to alarms off
        self.alarm_off = True
        # counter
        for i in range(2 * 60):
            self.BTN_ALARM.setText(str((2 * 60) - i - 1))
            sleep(1)

        # Reset Button
        self.BTN_ALARM.setStyleSheet('background-color: green')
        self.BTN_ALARM.setText('Alarm')
        self.BTN_ALARM.setEnabled(True)

        # set global to alarms on
        self.alarm_off = False
        # end thread
        sys.exit(1)

    def BTN_ALARM_clicked(self) -> None:
        print("DEBUG: ALARM pushed")
        thread_alarm = Thread(target=self.alarm_work)
        thread_alarm.start()

    def BTN_Credits_clicked(self) -> None:
        print("DEBUG: Credits pushed")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # sys.exit()
    os._exit(app.exec_())
