# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSlider, QFileDialog, QCheckBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

class ImageProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.image = None
        self.processed_image = None
        self.brightness = 50
        self.contrast = 50
        self.low_threshold = 50
        self.high_threshold = 150
        self.zoom_area_size = 100
        self.zoom_scale = 1.0
        self.focus_level = 0
        self.window_name = ""
        self.use_clahe = False

        self.btnLoadImage.clicked.connect(self.load_image)
        self.btnGrayscale.clicked.connect(self.apply_grayscale)
        self.btnEdgeDetected.clicked.connect(self.apply_edge_detection)
        self.btnSaveImage.clicked.connect(self.save_image)
        self.btnEnhanceContrast.clicked.connect(self.apply_contrast_enhancement)

        self.sliderBrightness.valueChanged.connect(self.update_brightness)
        self.sliderContrast.valueChanged.connect(self.update_contrast)
        self.sliderLowThreshold.valueChanged.connect(self.update_low_threshold)
        self.sliderHighThreshold.valueChanged.connect(self.update_high_threshold)
        self.sliderZoomSize.valueChanged.connect(self.update_zoom_size)

        self.checkboxCLAHE.stateChanged.connect(self.toggle_clahe)

    def setup_ui(self):
        self.setWindowTitle("Medical Image Processor")
        self.resize(900, 700)

        self.btnLoadImage = QPushButton("Load Image", self)
        self.btnLoadImage.setGeometry(20, 20, 100, 35)

        self.btnGrayscale = QPushButton("Apply Grayscale", self)
        self.btnGrayscale.setGeometry(130, 20, 120, 35)

        self.btnEdgeDetected = QPushButton("Edge Detection", self)
        self.btnEdgeDetected.setGeometry(260, 20, 120, 35)

        self.btnEnhanceContrast = QPushButton("Enhance Contrast", self)
        self.btnEnhanceContrast.setGeometry(390, 20, 120, 35)

        self.btnSaveImage = QPushButton("Save Image", self)
        self.btnSaveImage.setGeometry(520, 20, 100, 35)

        self.labelImage = QLabel(self)
        self.labelImage.setGeometry(20, 70, 550, 550)
        self.labelImage.setStyleSheet("border: 2px solid #333; background-color: #f0f0f0;")
        self.labelImage.setScaledContents(False)
        self.labelImage.setAlignment(Qt.AlignCenter)
        self.labelImage.setText("Load an image to start processing")

        y_offset = 80

        self.checkboxCLAHE = QCheckBox("Enable CLAHE Enhancement", self)
        self.checkboxCLAHE.setGeometry(600, y_offset, 200, 25)
        y_offset += 40

        self.labelBrightnessValue = QLabel("Brightness: 50", self)
        self.labelBrightnessValue.setGeometry(600, y_offset, 180, 25)
        y_offset += 30

        self.sliderBrightness = QSlider(Qt.Horizontal, self)
        self.sliderBrightness.setGeometry(600, y_offset, 200, 25)
        self.sliderBrightness.setMinimum(0)
        self.sliderBrightness.setMaximum(100)
        self.sliderBrightness.setValue(50)
        y_offset += 40

        self.labelContrastValue = QLabel("Contrast: 50", self)
        self.labelContrastValue.setGeometry(600, y_offset, 180, 25)
        y_offset += 30

        self.sliderContrast = QSlider(Qt.Horizontal, self)
        self.sliderContrast.setGeometry(600, y_offset, 200, 25)
        self.sliderContrast.setMinimum(0)
        self.sliderContrast.setMaximum(100)
        self.sliderContrast.setValue(50)
        y_offset += 40

        self.labelLowThreshold = QLabel("Low Threshold: 50", self)
        self.labelLowThreshold.setGeometry(600, y_offset, 180, 25)
        y_offset += 30

        self.sliderLowThreshold = QSlider(Qt.Horizontal, self)
        self.sliderLowThreshold.setGeometry(600, y_offset, 200, 25)
        self.sliderLowThreshold.setMinimum(0)
        self.sliderLowThreshold.setMaximum(255)
        self.sliderLowThreshold.setValue(50)
        y_offset += 40

        self.labelHighThreshold = QLabel("High Threshold: 150", self)
        self.labelHighThreshold.setGeometry(600, y_offset, 180, 25)
        y_offset += 30

        self.sliderHighThreshold = QSlider(Qt.Horizontal, self)
        self.sliderHighThreshold.setGeometry(600, y_offset, 200, 25)
        self.sliderHighThreshold.setMinimum(0)
        self.sliderHighThreshold.setMaximum(255)
        self.sliderHighThreshold.setValue(150)
        y_offset += 40

        self.labelZoomSize = QLabel("Zoom Area Size: 100", self)
        self.labelZoomSize.setGeometry(600, y_offset, 180, 25)
        y_offset += 30

        self.sliderZoomSize = QSlider(Qt.Horizontal, self)
        self.sliderZoomSize.setGeometry(600, y_offset, 200, 25)
        self.sliderZoomSize.setMinimum(20)
        self.sliderZoomSize.setMaximum(300)
        self.sliderZoomSize.setValue(100)
        y_offset += 40

        instructions = QLabel("Instructions:\n• Load medical image\n• Use sliders to adjust\n• Left-click for magnifier \n• Mouse wheel for focus control \n• Main image stays original during zoom\n• Enable CLAHE for better lesion visibility\n• Focus: Scroll up=Sharpen, Scroll down=Blur", self)
        instructions.setGeometry(600, 520, 250, 130)
        instructions.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #999999;
                border-radius: 5px;
                font-size: 10px;
            }
        """)
        instructions.setWordWrap(True)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Medical Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.tiff)")
        if file_path:
            try:
                with open(file_path, 'rb') as f:
                    file_bytes = f.read()
                nparr = np.frombuffer(file_bytes, np.uint8)
                self.image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                if self.image is not None:
                    self.processed_image = self.image.copy()
                    self.show_on_main_label(self.image)
                else:
                    print("Error: Could not decode image file")
            except Exception as e:
                print(f"Error loading image: {e}")
                try:
                    self.image = cv2.imread(file_path)
                    if self.image is not None:
                        self.processed_image = self.image.copy()
                        self.show_on_main_label(self.image)
                except Exception as e2:
                    print(f"Fallback method also failed: {e2}")

    def apply_focus_effect(self, img):
        if self.focus_level == 0:
            return img
        if self.focus_level < 0:
            blur_strength = abs(self.focus_level)
            kernel_size = min(blur_strength * 2 + 1, 15)
            if kernel_size % 2 == 0:
                kernel_size += 1
            return cv2.GaussianBlur(img, (kernel_size, kernel_size), blur_strength)
        else:
            sharpen_strength = self.focus_level / 10.0
            blurred = cv2.GaussianBlur(img, (9, 9), 10.0)
            unsharp_mask = cv2.subtract(img, blurred)
            return cv2.addWeighted(img, 1.0, unsharp_mask, sharpen_strength, 0)

    def apply_contrast_enhancement(self):
        if self.image is not None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) if len(self.image.shape) == 3 else self.image.copy()
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
            enhanced = clahe.apply(gray)
            alpha = self.contrast / 50.0
            beta = (self.brightness - 50) * 2
            enhanced = cv2.convertScaleAbs(enhanced, alpha=alpha, beta=beta)
            enhanced = self.apply_focus_effect(enhanced)
            self.processed_image = enhanced
            self.window_name = "Enhanced Contrast Result"
            self.show_interactive_window(self.window_name, enhanced)

    def apply_grayscale(self):
        if self.image is not None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) if len(self.image.shape) == 3 else self.image.copy()
            if self.use_clahe:
                clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                gray = clahe.apply(gray)
            alpha = self.contrast / 50.0
            beta = (self.brightness - 50) * 2
            adjusted = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
            adjusted = self.apply_focus_effect(adjusted)
            self.processed_image = adjusted
            self.window_name = "Grayscale Result"
            self.show_interactive_window(self.window_name, adjusted)

    def apply_edge_detection(self):
        if self.image is not None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) if len(self.image.shape) == 3 else self.image.copy()
            if self.use_clahe:
                clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                gray = clahe.apply(gray)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            edges = cv2.Canny(blurred, self.low_threshold, self.high_threshold)
            edges = self.apply_focus_effect(edges)
            self.processed_image = edges
            self.window_name = "Edge Detection Result"
            self.show_interactive_window(self.window_name, edges)

    def save_image(self):
        if self.processed_image is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Processed Image", "", "Images (*.png *.jpg *.jpeg)")
            if file_path:
                try:
                    is_success, buffer = cv2.imencode('.png', self.processed_image)
                    if is_success:
                        with open(file_path, 'wb') as f:
                            f.write(buffer)
                    else:
                        print("Error: Could not encode image for saving")
                except Exception as e:
                    print(f"Error saving image: {e}")
                    try:
                        cv2.imwrite(file_path, self.processed_image)
                    except Exception as e2:
                        print(f"Fallback save method also failed: {e2}")

    def update_brightness(self, value):
        self.brightness = value
        self.labelBrightnessValue.setText(f"Brightness: {value}")

    def update_contrast(self, value):
        self.contrast = value
        self.labelContrastValue.setText(f"Contrast: {value}")

    def update_low_threshold(self, value):
        self.low_threshold = value
        self.labelLowThreshold.setText(f"Low Threshold: {value}")

    def update_high_threshold(self, value):
        self.high_threshold = value
        self.labelHighThreshold.setText(f"High Threshold: {value}")

    def update_zoom_size(self, value):
        self.zoom_area_size = value
        self.labelZoomSize.setText(f"Zoom Area Size: {value}")

    def toggle_clahe(self, state):
        self.use_clahe = (state == 2)
        print(f"CLAHE enhancement: {'Enabled' if self.use_clahe else 'Disabled'}")

    def show_on_main_label(self, img):
        if len(img.shape) == 3:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img_rgb.shape
            qimg = QImage(img_rgb.data, w, h, ch * w, QImage.Format_RGB888)
        else:
            h, w = img.shape
            qimg = QImage(img.data, w, h, w, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(qimg).scaled(
            self.labelImage.width(),
            self.labelImage.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.labelImage.setPixmap(pixmap)

    def show_interactive_window(self, title, img):
        self.zoom_scale = 1.0
        clone = img.copy()
        cv2.namedWindow(title, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(title, 800, 800)

        def on_mouse(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                zoomed = self.get_zoomed_region(clone, x, y, self.zoom_area_size)
                if zoomed is not None and zoomed.size > 0:
                    self.show_zoom_in_main_label(zoomed)
            elif event == cv2.EVENT_MOUSEWHEEL:
                if flags > 0:
                    self.focus_level = min(10, self.focus_level + 1)
                else:
                    self.focus_level = max(-10, self.focus_level - 1)
                focused_img = self.apply_focus_effect(clone)
                cv2.imshow(title, focused_img)

        cv2.setMouseCallback(title, on_mouse)
        cv2.imshow(title, clone)
        cv2.waitKey(1)

    def show_zoom_in_main_label(self, zoomed_img):
        self.show_simple_zoom_window(zoomed_img)

    def show_simple_zoom_window(self, zoomed_img):
        zoom_window_name = "Zoomed Region"
        cv2.namedWindow(zoom_window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(zoom_window_name, 500, 500)
        cv2.imshow(zoom_window_name, zoomed_img)
        cv2.waitKey(1)

    def get_zoomed_region(self, img, x, y, size):
        if img is None or img.size == 0:
            return None
        h, w = img.shape[:2]
        half = size // 2
        x1 = max(0, x - half)
        y1 = max(0, y - half)
        x2 = min(w, x + half)
        y2 = min(h, y + half)
        if x2 <= x1 or y2 <= y1:
            return None
        zoomed = img[y1:y2, x1:x2]
        if zoomed.size == 0:
            return None
        try:
            if zoomed.shape[0] < 10 or zoomed.shape[1] < 10:
                zoomed = cv2.resize(zoomed, (50, 50), interpolation=cv2.INTER_NEAREST)
            zoomed = cv2.resize(zoomed, (400, 400), interpolation=cv2.INTER_CUBIC)
            return zoomed
        except cv2.error:
            return None

    def get_scaled_image(self, img, scale):
        if scale <= 0:
            scale = 0.1
        height, width = img.shape[:2]
        new_size = (int(width * scale), int(height * scale))
        if new_size[0] > 0 and new_size[1] > 0:
            return cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
        else:
            return img

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessor()
    window.show()
    sys.exit(app.exec())

