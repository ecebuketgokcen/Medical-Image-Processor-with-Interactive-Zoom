# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1064, 856)
        self.btnEdgeDetected = QPushButton(Widget)
        self.btnEdgeDetected.setObjectName(u"btnEdgeDetected")
        self.btnEdgeDetected.setGeometry(QRect(580, 50, 141, 31))
        self.btnSaveImage = QPushButton(Widget)
        self.btnSaveImage.setObjectName(u"btnSaveImage")
        self.btnSaveImage.setGeometry(QRect(840, 760, 151, 31))
        self.btnGrayscale = QPushButton(Widget)
        self.btnGrayscale.setObjectName(u"btnGrayscale")
        self.btnGrayscale.setGeometry(QRect(290, 50, 151, 31))
        self.btnLoadImage = QPushButton(Widget)
        self.btnLoadImage.setObjectName(u"btnLoadImage")
        self.btnLoadImage.setGeometry(QRect(50, 50, 131, 31))
        self.labelImage = QLabel(Widget)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setGeometry(QRect(110, 160, 311, 271))
        self.labelBrightnessValue = QLabel(Widget)
        self.labelBrightnessValue.setObjectName(u"labelBrightnessValue")
        self.labelBrightnessValue.setGeometry(QRect(60, 570, 141, 31))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 790, 151, 20))
        self.labelEdgeLowValue = QLabel(Widget)
        self.labelEdgeLowValue.setObjectName(u"labelEdgeLowValue")
        self.labelEdgeLowValue.setGeometry(QRect(60, 650, 151, 20))
        self.labelEdgeHighValue = QLabel(Widget)
        self.labelEdgeHighValue.setObjectName(u"labelEdgeHighValue")
        self.labelEdgeHighValue.setGeometry(QRect(60, 720, 161, 20))
        self.sliderBrightness = QSlider(Widget)
        self.sliderBrightness.setObjectName(u"sliderBrightness")
        self.sliderBrightness.setGeometry(QRect(270, 580, 160, 18))
        self.sliderBrightness.setOrientation(Qt.Orientation.Horizontal)
        self.sliderEdgeHigh = QSlider(Widget)
        self.sliderEdgeHigh.setObjectName(u"sliderEdgeHigh")
        self.sliderEdgeHigh.setGeometry(QRect(270, 720, 160, 18))
        self.sliderEdgeHigh.setOrientation(Qt.Orientation.Horizontal)
        self.sliderZoomSize = QSlider(Widget)
        self.sliderZoomSize.setObjectName(u"sliderZoomSize")
        self.sliderZoomSize.setGeometry(QRect(270, 790, 160, 18))
        self.sliderZoomSize.setOrientation(Qt.Orientation.Horizontal)
        self.sliderEdgeLow = QSlider(Widget)
        self.sliderEdgeLow.setObjectName(u"sliderEdgeLow")
        self.sliderEdgeLow.setGeometry(QRect(270, 650, 160, 18))
        self.sliderEdgeLow.setOrientation(Qt.Orientation.Horizontal)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btnEdgeDetected.setText(QCoreApplication.translate("Widget", u"Edge Detection", None))
        self.btnSaveImage.setText(QCoreApplication.translate("Widget", u"Save Image", None))
        self.btnGrayscale.setText(QCoreApplication.translate("Widget", u"Apply Grayscale", None))
        self.btnLoadImage.setText(QCoreApplication.translate("Widget", u"Load Image", None))
        self.labelImage.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.labelBrightnessValue.setText(QCoreApplication.translate("Widget", u"Brightness: 50", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Zoom Area Size: 100", None))
        self.labelEdgeLowValue.setText(QCoreApplication.translate("Widget", u"Low Threshold: 100", None))
        self.labelEdgeHighValue.setText(QCoreApplication.translate("Widget", u"High Threshold: 150", None))
    # retranslateUi

