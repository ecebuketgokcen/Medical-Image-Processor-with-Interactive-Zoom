# -*- coding: utf-8 -*-
import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSlider, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

class ImageProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.image = None
        self.processed_image = None
        self.brightness = 50
        self.low_threshold = 100
        self.high_threshold = 150
        self.zoom_area_size = 100
        self.zoom_scale = 1.0
        self.window_name = ""

        self.btnLoadImage.clicked.connect(self.load_image)
        self.btnGrayscale.clicked.connect(self.apply_grayscale)
        self.btnEdgeDetected.clicked.connect(self.apply_edge_detection)
        self.btnSaveImage.clicked.connect(self.save_image)

        self.sliderBrightness.valueChanged.connect(self.update_brightness)
        self.sliderLowThreshold.valueChanged.connect(self.update_low_threshold)
        self.sliderHighThreshold.valueChanged.connect(self.update_high_threshold)
        self.sliderZoomSize.valueChanged.connect(self.update_zoom_size)

    def setup_ui(self):
        self.setWindowTitle("Image Processor")
        self.resize(800, 600)

        self.btnLoadImage = QPushButton("Load Image", self)
        self.btnLoadImage.setGeometry(50, 30, 120, 30)

        self.btnGrayscale = QPushButton("Apply Grayscale", self)
        self.btnGrayscale.setGeometry(180, 30, 120, 30)

        self.btnEdgeDetected = QPushButton("Edge Detection", self)
        self.btnEdgeDetected.setGeometry(310, 30, 120, 30)

        self.btnSaveImage = QPushButton("Save Image", self)
        self.btnSaveImage.setGeometry(440, 30, 120, 30)

        self.labelImage = QLabel(self)
        self.labelImage.setGeometry(50, 80, 500, 480)
        self.labelImage.setStyleSheet("border: 1px solid black;")
        self.labelImage.setScaledContents(False)

        self.labelBrightnessValue = QLabel("Brightness: 50", self)
        self.labelBrightnessValue.setGeometry(580, 100, 180, 30)

        self.sliderBrightness = QSlider(Qt.Horizontal, self)
        self.sliderBrightness.setGeometry(580, 130, 180, 20)
        self.sliderBrightness.setMinimum(0)
        self.sliderBrightness.setMaximum(100)
        self.sliderBrightness.setValue(50)

        self.labelLowThreshold = QLabel("Low Threshold: 100", self)
        self.labelLowThreshold.setGeometry(580, 170, 180, 30)

        self.sliderLowThreshold = QSlider(Qt.Horizontal, self)
        self.sliderLowThreshold.setGeometry(580, 200, 180, 20)
        self.sliderLowThreshold.setMinimum(0)
        self.sliderLowThreshold.setMaximum(255)
        self.sliderLowThreshold.setValue(100)

        self.labelHighThreshold = QLabel("High Threshold: 150", self)
        self.labelHighThreshold.setGeometry(580, 240, 180, 30)

        self.sliderHighThreshold = QSlider(Qt.Horizontal, self)
        self.sliderHighThreshold.setGeometry(580, 270, 180, 20)
        self.sliderHighThreshold.setMinimum(0)
        self.sliderHighThreshold.setMaximum(255)
        self.sliderHighThreshold.setValue(150)

        self.labelZoomSize = QLabel("Zoom Area Size: 100", self)
        self.labelZoomSize.setGeometry(580, 310, 180, 30)

        self.sliderZoomSize = QSlider(Qt.Horizontal, self)
        self.sliderZoomSize.setGeometry(580, 340, 180, 20)
        self.sliderZoomSize.setMinimum(20)
        self.sliderZoomSize.setMaximum(300)
        self.sliderZoomSize.setValue(100)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image = cv2.imread(file_path)
            self.processed_image = self.image.copy()
            self.show_on_main_label(self.image)

    def apply_grayscale(self):
        if self.image is not None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            adjusted = cv2.convertScaleAbs(gray, alpha=self.brightness / 50.0)
            self.processed_image = adjusted
            self.window_name = "Grayscale Result"
            self.show_interactive_window(self.window_name, adjusted)

    def apply_edge_detection(self):
        if self.image is not None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, self.low_threshold, self.high_threshold)
            self.processed_image = edges
            self.window_name = "Edge Detection Result"
            self.show_interactive_window(self.window_name, edges)

    def save_image(self):
        if self.processed_image is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.jpeg)")
            if file_path:
                if len(self.processed_image.shape) == 2:
                    cv2.imwrite(file_path, self.processed_image)
                else:
                    cv2.imwrite(file_path, cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2BGR))

    def update_brightness(self, value):
        self.brightness = value
        self.labelBrightnessValue.setText(f"Brightness: {value}")

    def update_low_threshold(self, value):
        self.low_threshold = value
        self.labelLowThreshold.setText(f"Low Threshold: {value}")

    def update_high_threshold(self, value):
        self.high_threshold = value
        self.labelHighThreshold.setText(f"High Threshold: {value}")

    def update_zoom_size(self, value):
        self.zoom_area_size = value
        self.labelZoomSize.setText(f"Zoom Area Size: {value}")

    def show_on_main_label(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        qimg = QImage(img_rgb.data, w, h, ch * w, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg).scaled(
            self.labelImage.width(),
            self.labelImage.height(),
            Qt.KeepAspectRatio
        )
        self.labelImage.setPixmap(pixmap)

    def show_interactive_window(self, title, img):
        self.zoom_scale = 1.0
        clone = img.copy()
        cv2.namedWindow(title, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(title, 800, 900)

        def on_mouse(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                zoomed = self.get_zoomed_region(clone, x, y, self.zoom_area_size)
                cv2.imshow("Zoomed Region", zoomed)
            elif event == cv2.EVENT_MOUSEWHEEL:
                if flags > 0:
                    self.zoom_scale *= 1.1
                else:
                    self.zoom_scale /= 1.1
                zoomed = self.get_scaled_image(clone, self.zoom_scale)
                cv2.imshow(title, zoomed)

        cv2.setMouseCallback(title, on_mouse)
        cv2.imshow(title, clone)
        cv2.waitKey(1)

    def get_zoomed_region(self, img, x, y, size):
        h, w = img.shape[:2]
        half = size // 2
        x1 = max(0, x - half)
        y1 = max(0, y - half)
        x2 = min(w, x + half)
        y2 = min(h, y + half)
        zoomed = img[y1:y2, x1:x2]
        zoomed = cv2.resize(zoomed, (800, 800), interpolation=cv2.INTER_NEAREST)
        return zoomed

    def get_scaled_image(self, img, scale):
        height, width = img.shape[:2]
        new_size = (int(width * scale), int(height * scale))
        return cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessor()
    window.show()
    sys.exit(app.exec())

