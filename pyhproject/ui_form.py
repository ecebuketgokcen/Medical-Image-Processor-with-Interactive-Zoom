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
    QSlider, QWidget, QCheckBox)

class Ui_Widget(object):
    """
    UI Form class for Medical Image Processor
    
    This class defines the user interface layout generated from Qt Designer.
    Contains all the widgets and their initial properties for the medical
    image processing application.
    """
    
    def setupUi(self, Widget):
        """
        Set up the user interface for the Medical Image Processor
        
        Args:
            Widget: The main widget to set up the UI on
        """
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1064, 856)
        Widget.setWindowTitle("Medical Image Processor")
        
        # Main action buttons
        self.btnLoadImage = QPushButton(Widget)
        self.btnLoadImage.setObjectName(u"btnLoadImage")
        self.btnLoadImage.setGeometry(QRect(50, 50, 131, 31))
        
        self.btnGrayscale = QPushButton(Widget)
        self.btnGrayscale.setObjectName(u"btnGrayscale")
        self.btnGrayscale.setGeometry(QRect(290, 50, 151, 31))
        
        self.btnEdgeDetected = QPushButton(Widget)
        self.btnEdgeDetected.setObjectName(u"btnEdgeDetected")
        self.btnEdgeDetected.setGeometry(QRect(580, 50, 141, 31))
        
        self.btnEnhanceContrast = QPushButton(Widget)
        self.btnEnhanceContrast.setObjectName(u"btnEnhanceContrast")
        self.btnEnhanceContrast.setGeometry(QRect(730, 50, 151, 31))
        
        self.btnSaveImage = QPushButton(Widget)
        self.btnSaveImage.setObjectName(u"btnSaveImage")
        self.btnSaveImage.setGeometry(QRect(890, 50, 151, 31))
        
        # Main image display area
        self.labelImage = QLabel(Widget)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setGeometry(QRect(50, 100, 600, 400))
        self.labelImage.setStyleSheet("border: 2px solid #333; background-color: #f0f0f0;")
        self.labelImage.setScaledContents(False)
        self.labelImage.setAlignment(Qt.AlignCenter)
        self.labelImage.setText("Load an image to start processing")
        
        # CLAHE Enhancement checkbox
        self.checkboxCLAHE = QCheckBox(Widget)
        self.checkboxCLAHE.setObjectName(u"checkboxCLAHE")
        self.checkboxCLAHE.setGeometry(QRect(700, 120, 200, 25))
        
        # Control labels and sliders
        y_offset = 160
        
        # Brightness controls
        self.labelBrightnessValue = QLabel(Widget)
        self.labelBrightnessValue.setObjectName(u"labelBrightnessValue")
        self.labelBrightnessValue.setGeometry(QRect(700, y_offset, 180, 25))
        y_offset += 30
        
        self.sliderBrightness = QSlider(Widget)
        self.sliderBrightness.setObjectName(u"sliderBrightness")
        self.sliderBrightness.setGeometry(QRect(700, y_offset, 200, 25))
        self.sliderBrightness.setOrientation(Qt.Orientation.Horizontal)
        self.sliderBrightness.setMinimum(0)
        self.sliderBrightness.setMaximum(100)
        self.sliderBrightness.setValue(50)
        y_offset += 40
        
        # Contrast controls
        self.labelContrastValue = QLabel(Widget)
        self.labelContrastValue.setObjectName(u"labelContrastValue")
        self.labelContrastValue.setGeometry(QRect(700, y_offset, 180, 25))
        y_offset += 30
        
        self.sliderContrast = QSlider(Widget)
        self.sliderContrast.setObjectName(u"sliderContrast")
        self.sliderContrast.setGeometry(QRect(700, y_offset, 200, 25))
        self.sliderContrast.setOrientation(Qt.Orientation.Horizontal)
        self.sliderContrast.setMinimum(0)
        self.sliderContrast.setMaximum(100)
        self.sliderContrast.setValue(50)
        y_offset += 40
        
        # Edge detection low threshold
        self.labelEdgeLowValue = QLabel(Widget)
        self.labelEdgeLowValue.setObjectName(u"labelEdgeLowValue")
        self.labelEdgeLowValue.setGeometry(QRect(700, y_offset, 180, 25))
        y_offset += 30
        
        self.sliderEdgeLow = QSlider(Widget)
        self.sliderEdgeLow.setObjectName(u"sliderEdgeLow")
        self.sliderEdgeLow.setGeometry(QRect(700, y_offset, 200, 25))
        self.sliderEdgeLow.setOrientation(Qt.Orientation.Horizontal)
        self.sliderEdgeLow.setMinimum(0)
        self.sliderEdgeLow.setMaximum(255)
        self.sliderEdgeLow.setValue(50)
        y_offset += 40
        
        # Edge detection high threshold
        self.labelEdgeHighValue = QLabel(Widget)
        self.labelEdgeHighValue.setObjectName(u"labelEdgeHighValue")
        self.labelEdgeHighValue.setGeometry(QRect(700, y_offset, 180, 25))
        y_offset += 30
        
        self.sliderEdgeHigh = QSlider(Widget)
        self.sliderEdgeHigh.setObjectName(u"sliderEdgeHigh")
        self.sliderEdgeHigh.setGeometry(QRect(700, y_offset, 200, 25))
        self.sliderEdgeHigh.setOrientation(Qt.Orientation.Horizontal)
        self.sliderEdgeHigh.setMinimum(0)
        self.sliderEdgeHigh.setMaximum(255)
        self.sliderEdgeHigh.setValue(150)
        y_offset += 40
        
        # Zoom area size controls
        self.labelZoomSize = QLabel(Widget)
        self.labelZoomSize.setObjectName(u"labelZoomSize")
        self.labelZoomSize.setGeometry(QRect(700, y_offset, 180, 25))
        y_offset += 30
        
        self.sliderZoomSize = QSlider(Widget)
        self.sliderZoomSize.setObjectName(u"sliderZoomSize")
        self.sliderZoomSize.setGeometry(QRect(700, y_offset, 200, 25))
        self.sliderZoomSize.setOrientation(Qt.Orientation.Horizontal)
        self.sliderZoomSize.setMinimum(20)
        self.sliderZoomSize.setMaximum(300)
        self.sliderZoomSize.setValue(100)
        y_offset += 40
        
        # Instructions label
        self.labelInstructions = QLabel(Widget)
        self.labelInstructions.setObjectName(u"labelInstructions")
        self.labelInstructions.setGeometry(QRect(700, 520, 300, 150))
        self.labelInstructions.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #999999;
                border-radius: 5px;
                font-size: 10px;
            }
        """)
        self.labelInstructions.setWordWrap(True)

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        """
        Set up the text content for all UI elements
        
        Args:
            Widget: The main widget to set translations for
        """
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Medical Image Processor", None))
        
        # Button texts
        self.btnLoadImage.setText(QCoreApplication.translate("Widget", u"Load Image", None))
        self.btnGrayscale.setText(QCoreApplication.translate("Widget", u"Apply Grayscale", None))
        self.btnEdgeDetected.setText(QCoreApplication.translate("Widget", u"Edge Detection", None))
        self.btnEnhanceContrast.setText(QCoreApplication.translate("Widget", u"Enhance Contrast", None))
        self.btnSaveImage.setText(QCoreApplication.translate("Widget", u"Save Image", None))
        
        # Main image label
        self.labelImage.setText(QCoreApplication.translate("Widget", u"Load an image to start processing", None))
        
        # CLAHE checkbox
        self.checkboxCLAHE.setText(QCoreApplication.translate("Widget", u"Enable CLAHE Enhancement", None))
        
        # Control labels with default values
        self.labelBrightnessValue.setText(QCoreApplication.translate("Widget", u"Brightness: 50", None))
        self.labelContrastValue.setText(QCoreApplication.translate("Widget", u"Contrast: 50", None))
        self.labelEdgeLowValue.setText(QCoreApplication.translate("Widget", u"Low Threshold: 50", None))
        self.labelEdgeHighValue.setText(QCoreApplication.translate("Widget", u"High Threshold: 150", None))
        self.labelZoomSize.setText(QCoreApplication.translate("Widget", u"Zoom Area Size: 100", None))
        
        # Instructions text
        instructions_text = """Instructions:
• Load medical image
• Use sliders to adjust
• Left-click for magnifier 
• Mouse wheel for focus control 
• Main image stays original during zoom
• Enable CLAHE for better lesion visibility
• Focus: Scroll up=Sharpen, Scroll down=Blur"""
        
        self.labelInstructions.setText(QCoreApplication.translate("Widget", instructions_text, None))
        
        # Set tooltips for better user experience
        self.btnLoadImage.setToolTip(QCoreApplication.translate("Widget", u"Load a medical image file (PNG, JPG, TIFF, BMP)", None))
        self.btnGrayscale.setToolTip(QCoreApplication.translate("Widget", u"Convert image to grayscale for analysis", None))
        self.btnEdgeDetected.setToolTip(QCoreApplication.translate("Widget", u"Apply Canny edge detection algorithm", None))
        self.btnEnhanceContrast.setToolTip(QCoreApplication.translate("Widget", u"Apply CLAHE contrast enhancement", None))
        self.btnSaveImage.setToolTip(QCoreApplication.translate("Widget", u"Save the processed image", None))
        
        self.checkboxCLAHE.setToolTip(QCoreApplication.translate("Widget", u"Enable Contrast Limited Adaptive Histogram Equalization for better medical image contrast", None))
        
        self.sliderBrightness.setToolTip(QCoreApplication.translate("Widget", u"Adjust image brightness (0-100)", None))
        self.sliderContrast.setToolTip(QCoreApplication.translate("Widget", u"Adjust image contrast (0-100)", None))
        self.sliderEdgeLow.setToolTip(QCoreApplication.translate("Widget", u"Lower threshold for edge detection (0-255)", None))
        self.sliderEdgeHigh.setToolTip(QCoreApplication.translate("Widget", u"Upper threshold for edge detection (0-255)", None))
        self.sliderZoomSize.setToolTip(QCoreApplication.translate("Widget", u"Size of the zoom region in pixels (20-300)", None))
    # retranslateUi

