### _**Medical Image Processor with Interactive Zoom**_


[🧠 **Project Description**](url)

Medical Image Processor with Interactive Zoom & Focus Control is an advanced Python-based GUI application developed using PySide 6 and OpenCV. Designed specifically for medical image analysis, this application provides comprehensive image processing capabilities including grayscale conversion, edge detection, contrast enhancement, and interactive zoom functionality. The application features sophisticated focus control through mouse wheel interaction and includes CLAHE (Contrast Limited Adaptive Histogram Equalization) enhancement for improved lesion visibility in medical images.
Key innovations include real-time focus adjustment (sharpening/blurring), intelligent zoom with magnifier tool, and specialized medical imaging enhancements. The application maintains the original image in the main display while providing detailed analysis in separate interactive windows.

This project was developed as part of the Computational Methods in Engineering course at Ankara University, Department of Biomedical Engineering.

[✨ **Features**](url)

**🖼️ Image Upload & Support:**

Load PNG, JPEG, JPG, BMP, and TIFF images through user-friendly file dialog
Enhanced file handling with support for Unicode/Turkish file paths
Robust error handling and fallback loading methods

**🔄 Advanced Image Processing:**

Grayscale Conversion: Convert medical images to grayscale with dynamic brightness control
Edge Detection: Advanced Canny edge detection with real-time threshold adjustment and pre-processing
Contrast Enhancement: Dedicated contrast enhancement with automatic CLAHE application
CLAHE Enhancement: Optional Contrast Limited Adaptive Histogram Equalization for better lesion visibility (toggle on/off)

**🎛️ Real-time Controls:**

Brightness Control: Fine-tune image brightness (0-100 range)
Contrast Control: Dynamic contrast adjustment (0-100 range)
Edge Detection Thresholds: Separate low (0-255) and high (0-255) threshold controls for Canny edge detection
Zoom Area Size: Adjustable zoom region size (20-300 pixels)

**🔍 Interactive Focus & Zoom System:**

Focus Control: Scroll mouse wheel to adjust image sharpness (-10 to +10 levels)

Scroll up: Sharpen image with unsharp mask technique
Scroll down: Apply Gaussian blur for softer focus


**Interactive Zoom:** Click anywhere on the image to activate magnifier tool
Smart Zoom Display: Zoom opens in separate window while maintaining original image in main display
Region Selection: Intelligent boundary detection and region extraction

**💾 Enhanced Saving:**

Save processed images in PNG, JPEG formats
Unicode path support for international file names
Robust saving with fallback methods

**🎯 Medical Imaging Optimizations:**

CLAHE enhancement specifically designed for medical imaging
Gaussian blur pre-processing for smoother edge detection
Unsharp mask sharpening for better detail enhancement
Optimized for lesion and abnormality detection


[**Installation**](url)

**Clone the repository:**
`bash git clone `https://github.com/ecebuketgokcen/Medical-Image-Processor-with-Interactive-Zoom.git`

`cd Medical-Image-Processor-with-Interactive-Zoom`

Install dependencies: bash `pip install -r requirements.txt `

install manually: bash `pip install PySide6 opencv-python numpy`

[**Usage**](url)

Run the application using: bash `python main.py`

**Basic Workflow:**

Load Image: Click "Load Image" to select a medical image from your computer
Choose Enhancement: Enable "CLAHE Enhancement" checkbox for better lesion visibility (optional)
Apply Processing: Use "Apply Grayscale", "Edge Detection", or "Enhance Contrast" buttons
Adjust Parameters: Use sliders to fine-tune brightness, contrast, and thresholds in real-time
Interactive Analysis:

   Focus Control: Scroll mouse wheel over processed image to adjust sharpness/blur
   Zoom Analysis: Left-click on any region to open magnified view (400x400 pixels)
Save Results: Click "Save Image" to export processed version

**Advanced Features:**

CLAHE Enhancement: Toggle on for medical images with poor contrast
Focus Levels: -10 (maximum blur) to +10 (maximum sharpening)
Zoom Area Control: Adjust zoom region size before clicking for magnification
Multi-Window Analysis: Original stays in main window, zoom opens separately



[**Screenshots**](url)

**Main Application Interface**

![mainwindow](https://github.com/user-attachments/assets/34e40f92-1813-4b3a-92d7-ea5f74b6e044)
Medical Image Processor main interface with chest X-ray loaded and real-time control panels



**Grayscale Processing with Interactive Magnifier** 

![grayscale2](https://github.com/user-attachments/assets/15905775-bf3f-4a78-b6f1-bc39b1cf3d52)
![graysacel1](https://github.com/user-attachments/assets/c5cd9190-4bca-4cbc-92b3-169e3d8368ec)



**Edge Detection Results**

![edge detection](https://github.com/user-attachments/assets/bd5523e2-5b0b-4c5c-82df-b23153c62f63)
Advanced Canny edge detection with real-time threshold adjustment showing anatomical boundaries


**Zoomed Region-Real-time Processing with Multiple Windows**

![zoomed](https://github.com/user-attachments/assets/6fa96bce-181b-4820-be61-664e493e03d1)
![zoomedarea](https://github.com/user-attachments/assets/8170dd2a-3ae5-4c57-82b2-cdf39df8853b)
4x magnified region showing detailed anatomical structures with enhanced contrast for precise medical diagnosis



[📝**Notes**](url)

**Image Processing Algorithms:**

CLAHE: Contrast Limited Adaptive Histogram Equalization with 8x8 tile grid
Edge Detection: Canny algorithm with Gaussian blur pre-processing
Focus Control: Unsharp mask for sharpening, Gaussian blur for defocus
Zoom: Cubic interpolation for high-quality magnification

**Key Improvements:**

Unicode file path support for international users
Robust error handling with fallback methods
Memory-efficient image processing
Real-time parameter adjustment without reloading
Separate zoom windows to preserve original view

**Requirements & Notes**
System Requirements:

Python 3.7+
PySide6
OpenCV (cv2)
NumPy

CLAHE enhancement is optional - enable for medical images with poor contrast
Focus control works in real-time on processed images
Zoom tool works on any region of the processed image
All processing maintains original image quality
Supports Unicode file paths (Turkish characters, etc.)

**Troubleshooting:**

If images won't load, check file format compatibility
For Turkish/Unicode paths, the application includes automatic fallback handling
Ensure all dependencies are properly installed
Ensure your system has a proper Python environment setup before running the application. If you encounter issues, check that all dependencies (such as PySide6 and OpenCV) are correctly installed.



[**Contributing**](url)

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements. Areas for potential enhancement:

Additional medical imaging algorithms
More zoom levels and pan functionality
Batch processing capabilities
Advanced filtering options
Export format options

