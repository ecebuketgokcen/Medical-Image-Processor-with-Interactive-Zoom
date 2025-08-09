"""
Medical Image Processor with Interactive Zoom

Author: Ece Buket Gökçen
Department: Biomedical Engineering, Ankara University
"""

# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np
from pathlib import Path
from typing import Optional
import os

if sys.platform == "win32":
    try:
        os.system("chcp 65001")
    except:
        pass

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSlider, QFileDialog, QCheckBox, QMessageBox
from PySide6.QtGui import QPixmap, QImage, QFont
from PySide6.QtCore import Qt

class ZoomWindow(QWidget):

    def __init__(self, image: np.ndarray, title: str = "Magnified Region"):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 500, 500)
        self.setup_zoom_ui()
        self.display_zoomed_image(image)

    def setup_zoom_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: white;
            }
            QLabel {
                border: 2px solid #34495e;
                border-radius: 8px;
                background-color: #ecf0f1;
                padding: 5px;
            }
        """)

        self.zoom_label = QLabel(self)
        self.zoom_label.setGeometry(25, 25, 450, 450)
        self.zoom_label.setAlignment(Qt.AlignCenter)

    def display_zoomed_image(self, cv_image: np.ndarray):
        if cv_image is None or cv_image.size == 0:
            self.zoom_label.setText("No image data available")
            return

        try:
            if len(cv_image.shape) == 3:
                height, width, channels = cv_image.shape
                bytes_per_line = width * channels
                qt_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            else:
                height, width = cv_image.shape
                bytes_per_line = width
                qt_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(qt_image)
            scaled_pixmap = pixmap.scaled(440, 440, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.zoom_label.setPixmap(scaled_pixmap)

        except Exception as e:
            self.zoom_label.setText(f"Display error: {str(e)}")

class ImageProcessor(QWidget):

    def __init__(self):
        super().__init__()
        self.image: Optional[np.ndarray] = None
        self.processed_image: Optional[np.ndarray] = None

        self.brightness = 50
        self.contrast = 50
        self.low_threshold = 50
        self.high_threshold = 150
        self.zoom_area_size = 100
        self.zoom_scale = 1.0
        self.focus_level = 0
        self.window_name = ""
        self.use_clahe = False

        self.zoom_windows = []

        self.setup_ui()
        self.connect_signals()
        self.apply_modern_styling()

    def setup_ui(self):
        self.setWindowTitle("Medical Image Processor")
        self.resize(1100, 750)
        self.setMinimumSize(900, 600)

        button_configs = [
            ("Load Medical Image", 20, 20, 140, 40, self.load_image),
            ("Apply Grayscale", 170, 20, 140, 40, self.apply_grayscale),
            ("Edge Detection", 320, 20, 140, 40, self.apply_edge_detection),
            ("Enhance Contrast", 470, 20, 140, 40, self.apply_contrast_enhancement),
            ("Save Processed", 620, 20, 140, 40, self.save_image)
        ]

        for text, x, y, w, h, callback in button_configs:
            btn = QPushButton(text, self)
            btn.setGeometry(x, y, w, h)
            btn.clicked.connect(callback)
            setattr(self, f'btn{text.split()[-1]}', btn)

        self.labelImage = QLabel(self)
        self.labelImage.setGeometry(20, 80, 650, 580)
        self.labelImage.setStyleSheet("""
            QLabel {
                border: 3px solid #34495e;
                background-color: #ecf0f1;
                border-radius: 10px;
                color: #7f8c8d;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        self.labelImage.setScaledContents(False)
        self.labelImage.setAlignment(Qt.AlignCenter)
        self.labelImage.setText("Load medical image to begin processing")

        self.create_control_panel()
        self.create_status_panel()

    def create_control_panel(self):
        x_start, y_start = 690, 90

        self.checkboxCLAHE = QCheckBox("Enable CLAHE Enhancement", self)
        self.checkboxCLAHE.setGeometry(x_start, y_start, 280, 30)
        self.checkboxCLAHE.setToolTip("Contrast Limited Adaptive Histogram Equalization\nfor medical lesion detection")

        controls = [
            ("Brightness Control", "labelBrightnessValue", "sliderBrightness", 0, 100, 50, y_start + 50),
            ("Contrast Control", "labelContrastValue", "sliderContrast", 0, 100, 50, y_start + 120),
            ("Low Threshold (Canny)", "labelLowThreshold", "sliderLowThreshold", 0, 255, 50, y_start + 190),
            ("High Threshold (Canny)", "labelHighThreshold", "sliderHighThreshold", 0, 255, 150, y_start + 260),
            ("Zoom Region Size", "labelZoomSize", "sliderZoomSize", 20, 300, 100, y_start + 330)
        ]

        for title, label_attr, slider_attr, min_val, max_val, default, y_pos in controls:
            label = QLabel(f"{title}: {default}", self)
            label.setGeometry(x_start, y_pos, 250, 25)
            label.setFont(QFont("Arial", 10, QFont.Bold))
            label.setStyleSheet("color: black; font-weight: bold;")
            setattr(self, label_attr, label)

            slider = QSlider(Qt.Horizontal, self)
            slider.setGeometry(x_start, y_pos + 25, 280, 25)
            slider.setMinimum(min_val)
            slider.setMaximum(max_val)
            slider.setValue(default)
            setattr(self, slider_attr, slider)

    def create_status_panel(self):
        instructions = QLabel(""" Medical Image Processing Features:

• CLAHE enhancement for lesion visibility
• Real-time Canny edge detection with adaptive thresholds
• Interactive magnification (left-click on processed image)
• Focus control (mouse wheel: sharp/blur)
• Unsharp mask sharpening algorithm
• Image export capabilities

[Info] Usage: Load image → Adjust parameters → Apply processing
[Zoom] Analysis: Click processed image for magnification
[Focus] Control: Use mouse wheel on processed image for control""", self)

        instructions.setGeometry(680, 480, 400, 210)
        instructions.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                color: #2c3e50;
                padding: 15px;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                font-size: 11px;
                line-height: 1.4;
            }
        """)
        instructions.setWordWrap(True)

    def connect_signals(self):
        self.sliderBrightness.valueChanged.connect(self.update_brightness)
        self.sliderContrast.valueChanged.connect(self.update_contrast)
        self.sliderLowThreshold.valueChanged.connect(self.update_low_threshold)
        self.sliderHighThreshold.valueChanged.connect(self.update_high_threshold)
        self.sliderZoomSize.valueChanged.connect(self.update_zoom_size)

        self.checkboxCLAHE.stateChanged.connect(self.toggle_clahe)

    def apply_modern_styling(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f6fa;
                font-family: 'Segoe UI', Arial, sans-serif;
            }

            QLabel {
                color: black;
                font-weight: bold;
            }

            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 12px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 11px;
            }

            QPushButton:hover {
                background-color: #2980b9;
            }

            QPushButton:pressed {
                background-color: #21618c;
            }

            QSlider::groove:horizontal {
                border: 1px solid #bdc3c7;
                height: 8px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e1e1e1, stop:1 #ffffff);
                margin: 2px 0;
                border-radius: 4px;
            }

            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3498db, stop:1 #2980b9);
                border: 1px solid #2980b9;
                width: 18px;
                margin: -2px 0;
                border-radius: 9px;
            }

            QSlider::handle:horizontal:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5dade2, stop:1 #3498db);
            }

            QCheckBox {
                font-weight: bold;
                color: black;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }

            QCheckBox::indicator:unchecked {
                border: 2px solid #bdc3c7;
                background-color: white;
                border-radius: 3px;
            }

            QCheckBox::indicator:checked {
                border: 2px solid #27ae60;
                background-color: #27ae60;
                border-radius: 3px;
            }
        """)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Medical Image",
            "",
            "Medical Images (*.png *.jpg *.jpeg *.bmp *.tiff *.dcm);;All Files (*)"
        )

        if file_path:
            try:
                image_path = Path(file_path)

                with open(image_path, 'rb') as f:
                    file_bytes = f.read()

                nparr = np.frombuffer(file_bytes, np.uint8)
                self.image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                if self.image is not None:
                    self.processed_image = self.image.copy()
                    self.show_on_main_label(self.image)

                    height, width = self.image.shape[:2]
                    print(f"[OK] Medical image loaded: {image_path.name}")
                    print(f"   Dimensions: {width}x{height} pixels")
                    print(f"   Channels: {self.image.shape[2] if len(self.image.shape) == 3 else 1}")
                else:
                    raise ValueError("Could not decode medical image file")

            except Exception as e:
                print(f"[ERROR] Error loading medical image: {e}")
                QMessageBox.critical(self, "Image Loading Error",
                                   f"Could not load medical image:\n{str(e)}\n\nPlease check file format and try again.")

    def apply_focus_effect(self, img: np.ndarray) -> np.ndarray:
        if self.focus_level == 0:
            return img

        if self.focus_level < 0:
            blur_strength = abs(self.focus_level)
            kernel_size = min(blur_strength * 2 + 1, 15)
            if kernel_size % 2 == 0:
                kernel_size += 1
            blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), blur_strength)
            return blurred
        else:
            sharpen_strength = self.focus_level / 10.0

            blurred = cv2.GaussianBlur(img, (9, 9), 10.0)
            unsharp_mask = cv2.subtract(img, blurred)
            sharpened = cv2.addWeighted(img, 1.0, unsharp_mask, sharpen_strength, 0)

            return sharpened

    def apply_contrast_enhancement(self):
        if self.image is not None:
            try:
                if len(self.image.shape) == 3:
                    gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
                else:
                    gray = self.image.copy()

                clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
                enhanced = clahe.apply(gray)
                print("CLAHE enhancement applied for medical analysis")

                alpha = self.contrast / 50.0
                beta = (self.brightness - 50) * 2
                enhanced = cv2.convertScaleAbs(enhanced, alpha=alpha, beta=beta)

                enhanced = self.apply_focus_effect(enhanced)

                self.processed_image = enhanced
                self.window_name = "Enhanced Medical Image"
                self.show_interactive_window(self.window_name, enhanced)

            except Exception as e:
                QMessageBox.warning(self, "Processing Error", f"Enhancement failed: {str(e)}")

    def apply_grayscale(self):
        if self.image is not None:
            try:
                if len(self.image.shape) == 3:
                    gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
                else:
                    gray = self.image.copy()

                if self.use_clahe:
                    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                    gray = clahe.apply(gray)
                    print(" CLAHE enhancement applied to grayscale conversion")
                else:
                    print(" Standard grayscale conversion applied")

                alpha = self.contrast / 50.0
                beta = (self.brightness - 50) * 2
                adjusted = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

                adjusted = self.apply_focus_effect(adjusted)

                self.processed_image = adjusted
                self.window_name = "Grayscale Medical Analysis"
                self.show_interactive_window(self.window_name, adjusted)

            except Exception as e:
                QMessageBox.warning(self, "Processing Error", f"Grayscale conversion failed: {str(e)}")

    def apply_edge_detection(self):
        if self.image is not None:
            try:
                if len(self.image.shape) == 3:
                    gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
                else:
                    gray = self.image.copy()

                if self.use_clahe:
                    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                    gray = clahe.apply(gray)
                    print(" CLAHE preprocessing applied for edge detection")

                blurred = cv2.GaussianBlur(gray, (5, 5), 0)

                edges = cv2.Canny(blurred, self.low_threshold, self.high_threshold)

                edges = self.apply_focus_effect(edges)

                self.processed_image = edges
                self.window_name = "Medical Edge Detection"
                self.show_interactive_window(self.window_name, edges)

                print(f" Edge detection completed (Thresholds: {self.low_threshold}/{self.high_threshold})")

            except Exception as e:
                QMessageBox.warning(self, "Processing Error", f"Edge detection failed: {str(e)}")

    def save_image(self):
        if self.processed_image is not None:
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Processed Medical Image",
                "processed_medical_image.png",
                "PNG Files (*.png);;JPEG Files (*.jpg);;TIFF Files (*.tiff)"
            )

            if file_path:
                try:
                    save_path = Path(file_path)
                    is_success, buffer = cv2.imencode('.png', self.processed_image)

                    if is_success:
                        with open(save_path, 'wb') as f:
                            f.write(buffer)
                        print(f"[Save] Processed medical image saved: {save_path.name}")
                        QMessageBox.information(self, "Export Successful",
                                              f"Medical image saved:\n{save_path.name}")
                    else:
                        raise ValueError("Could not encode processed image")

                except Exception as e:
                    print(f" Error saving processed image: {e}")
                    QMessageBox.critical(self, "Save Error", f"Could not save image:\n{str(e)}")
        else:
            QMessageBox.warning(self, "No Image", "No processed image available to save.\nPlease process an image first.")

    def update_brightness(self, value):
        self.brightness = value
        self.labelBrightnessValue.setText(f"Brightness Control: {value}")

    def update_contrast(self, value):
        self.contrast = value
        self.labelContrastValue.setText(f"Contrast Control: {value}")

    def update_low_threshold(self, value):
        self.low_threshold = value
        self.labelLowThreshold.setText(f"Low Threshold (Canny): {value}")

    def update_high_threshold(self, value):
        self.high_threshold = value
        self.labelHighThreshold.setText(f"High Threshold (Canny): {value}")

    def update_zoom_size(self, value):
        self.zoom_area_size = value
        self.labelZoomSize.setText(f"Zoom Region Size: {value}")

    def toggle_clahe(self, state):
        self.use_clahe = (state == 2)
        status = "ENABLED" if self.use_clahe else "DISABLED"
        print(f" CLAHE Enhancement {status} - Medical imaging optimization")

    def show_on_main_label(self, img):
        if len(img.shape) == 3:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img_rgb.shape
            qimg = QImage(img_rgb.data, w, h, ch * w, QImage.Format_RGB888)
        else:
            h, w = img.shape
            qimg = QImage(img.data, w, h, w, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(qimg).scaled(
            self.labelImage.width() - 20,
            self.labelImage.height() - 20,
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
                    zoom_window = ZoomWindow(zoomed, f"Medical Analysis - {title}")
                    self.zoom_windows.append(zoom_window)
                    zoom_window.show()
                    print(f" Magnified region at ({x}, {y}) - Size: {self.zoom_area_size}px")

            elif event == cv2.EVENT_MOUSEWHEEL:
                if flags > 0:
                    self.focus_level = min(10, self.focus_level + 1)
                    focus_action = "Sharpened"
                else:
                    self.focus_level = max(-10, self.focus_level - 1)
                    focus_action = "Blurred"

                focused_img = self.apply_focus_effect(clone)
                cv2.imshow(title, focused_img)

                focus_text = ("Optimal Focus" if self.focus_level == 0 else
                            f"Blur Level {abs(self.focus_level)}" if self.focus_level < 0 else
                            f"Sharpen Level {self.focus_level}")
                print(f"[Focus] Focus {focus_action}: {focus_text}")

        cv2.setMouseCallback(title, on_mouse)
        cv2.imshow(title, clone)
        cv2.waitKey(1)

    def get_zoomed_region(self, img, x, y, size):
        if img is None or img.size == 0:
            print("[ERROR] Error: Invalid image for magnification")
            return None

        h, w = img.shape[:2]
        half = size // 2

        x1 = max(0, x - half)
        y1 = max(0, y - half)
        x2 = min(w, x + half)
        y2 = min(h, y + half)

        if x2 <= x1 or y2 <= y1:
            print(" Error: Invalid magnification region")
            return None

        zoomed = img[y1:y2, x1:x2]

        if zoomed.size == 0:
            print(" Error: Empty magnification region")
            return None

        try:
            if zoomed.shape[0] < 10 or zoomed.shape[1] < 10:
                zoomed = cv2.resize(zoomed, (50, 50), interpolation=cv2.INTER_NEAREST)

            zoomed = cv2.resize(zoomed, (400, 400), interpolation=cv2.INTER_CUBIC)
            return zoomed

        except cv2.error as e:
            print(f" Error creating magnified region: {e}")
            return None

    def closeEvent(self, event):
        try:
            cv2.destroyAllWindows()
            for window in self.zoom_windows:
                if window.isVisible():
                    window.close()
            print(" Medical Image Processor closed successfully")
            event.accept()
        except Exception as e:
            print(f" Cleanup warning: {e}")
            event.accept()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setApplicationName("Medical Image Processor")
        app.setApplicationVersion("2.0")

        window = ImageProcessor()
        window.show()

        print(" Medical Image Processor Started")

        sys.exit(app.exec())

    except Exception as e:
        print(f" Application startup error: {e}")
        sys.exit(1)
