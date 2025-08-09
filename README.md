 ### _**Medical Image Processor with Interactive Zoom**_


## 🧠Project Description 

Medical Image Processor with Interactive Zoom & Focus Control is an advanced Python-based GUI application developed using PySide 6 and OpenCV. Designed specifically for medical image analysis, this application provides comprehensive image processing capabilities including grayscale conversion, edge detection, contrast enhancement, and interactive zoom functionality. The application features sophisticated focus control through mouse wheel interaction and includes CLAHE (Contrast Limited Adaptive Histogram Equalization) enhancement for improved lesion visibility in medical images.
Key innovations include real-time focus adjustment (sharpening/blurring), intelligent zoom with magnifier tool, and specialized medical imaging enhancements. The application maintains the original image in the main display while providing detailed analysis in separate interactive windows.

This project was developed as part of the Computational Methods in Engineering course at Ankara University, Department of Biomedical Engineering.


## ✨Features

**🖼️ Image Upload & Support:**
- Multi-format medical image loading (PNG, JPEG, JPG, BMP, TIFF)
- Professional file handling with comprehensive error management
- User-friendly interface with clear feedback and recovery options

**🔄 Advanced Image Processing:**
- Grayscale Conversion: Convert medical images to grayscale with dynamic brightness control  
- Edge Detection: Advanced Canny edge detection with real-time threshold adjustment and pre-processing  
- Contrast Enhancement: Professional CLAHE enhancement with automatic application
- CLAHE Enhancement: Optional Contrast Limited Adaptive Histogram Equalization for better lesion visibility (toggle on/off)  

**🎛️ Real-time Controls:**
- Brightness Control: Fine-tune image brightness (0-100 range)  
- Contrast Control: Dynamic contrast adjustment (0-100 range)  
- Edge Detection Thresholds: Separate low (0-255) and high (0-255) threshold controls for Canny edge detection  
- Zoom Area Size: Adjustable zoom region size (20-300 pixels)  

**🔍 Interactive Focus & Zoom System:**
- Focus Control: Scroll mouse wheel to adjust image sharpness (-10 to +10 levels)  
  - Scroll up: Sharpen image with unsharp mask technique  
  - Scroll down: Apply Gaussian blur for softer focus  
- Interactive Zoom: Click anywhere on the image to activate magnifier tool  
- Smart Zoom Display: Zoom opens in separate window while maintaining original image in main display  
- Region Selection: Intelligent boundary detection and region extraction  

**💾 Enhanced Saving:**
- Save processed images in PNG, JPEG formats  
- Unicode path support for international file names  
- Robust saving with fallback methods  

**🎯 Medical Imaging Optimizations:**
- CLAHE enhancement specifically designed for medical imaging  
- Gaussian blur pre-processing for smoother edge detection  
- Unsharp mask sharpening for better detail enhancement  
- Optimized for lesion and abnormality detection  


## Installation

Clone the repository:
```bash
git clone https://github.com/ecebuketgokcen/Medical-Image-Processor-with-Interactive-Zoom.git
cd Medical-Image-Processor-with-Interactive-Zoom
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Install manually:
```bash
pip install PySide6 opencv-python numpy
```

## Usage

Run the application using: 
```bash
python main.py
```

**Basic Workflow:**
- **Load Image:** Click "Load Medical Image" to select a medical image from your computer  
- **Choose Enhancement:** Enable "CLAHE Enhancement" checkbox for better lesion visibility (optional)  
- **Apply Processing:** Use "Apply Grayscale", "Edge Detection", or "Enhance Contrast" buttons  
- **Adjust Parameters:** Use sliders to fine-tune brightness, contrast, and thresholds in real-time  
- **Interactive Analysis:**  
  - Focus Control: Scroll mouse wheel over processed image to adjust sharpness/blur  
  - Zoom Analysis: Left-click on any region to open magnified view (400x400 pixels)  
- **Save Results:** Click "Save Processed" to export processed version  

**Advanced Features:**
- **CLAHE Enhancement:** Toggle on for medical images with poor contrast  
- **Focus Levels:** -10 (maximum blur) to +10 (maximum sharpening)  
- **Zoom Area Control:** Adjust zoom region size before clicking for magnification  
- **Multi-Window Analysis:** Original stays in main window, zoom opens separately  




## Screenshots

## Main Application Interface

<img width="1370" height="963" alt="mainwindow" src="https://github.com/user-attachments/assets/560358ab-f1b8-40dc-a800-3e5725df6f0f" />

Medical Image Processor main interface with chest X-ray loaded and real-time control panels.


## Grayscale Processing with Interactive Magnifier 

<img width="1917" height="960" alt="1grayscale" src="https://github.com/user-attachments/assets/9162ec74-f421-46fa-b58b-b1eca6e6a249" />
<img width="1906" height="975" alt="3grayscale" src="https://github.com/user-attachments/assets/fd7ce486-39d1-441b-bcbc-8fbb6425bc2e" />
<img width="1917" height="975" alt="2grayscale" src="https://github.com/user-attachments/assets/1ec7d470-c10a-444a-b54c-18fcdef86876" />


## Edge Detection Results

<img width="1904" height="961" alt="1edge" src="https://github.com/user-attachments/assets/88004618-0c2d-4f6c-a45a-6ba061908e54" />

Advanced Canny edge detection with real-time threshold adjustment showing anatomical boundaries.


## Zoomed Region-Real-time Processing with Multiple Windows

<img width="1918" height="1002" alt="zoomed2" src="https://github.com/user-attachments/assets/1ed8d4dc-c8f0-4268-ab07-23378e697760" />
<img width="1912" height="994" alt="zoomed1" src="https://github.com/user-attachments/assets/9b128aca-b3b9-456e-a9dd-543cd31ea3bc" />

4x magnified region showing detailed anatomical structures with enhanced contrast for precise medical diagnosis.

## Enhance Contrast

<img width="1912" height="965" alt="2enhance" src="https://github.com/user-attachments/assets/a902b95d-2813-4b6a-8a26-bac30eadc225" />
<img width="1915" height="978" alt="1enhance" src="https://github.com/user-attachments/assets/bb37d439-500a-4e35-86f3-f0b18b784016" />
CLAHE enhancement algorithm automatically optimizes medical image contrast for improved lesion visibility and diagnostic accuracy.


## 📝Notes

## Image Processing Algorithms

- **CLAHE:** Contrast Limited Adaptive Histogram Equalization with 8x8 tile grid  
- **Edge Detection:** Canny algorithm with Gaussian blur pre-processing  
- **Focus Control:** Unsharp mask for sharpening, Gaussian blur for defocus  
- **Zoom:** Cubic interpolation for high-quality magnification  

## Key Improvements

- Unicode file path support for international users  
- Robust error handling with fallback methods  
- Memory-efficient image processing  
- Real-time parameter adjustment without reloading  
- Separate zoom windows to preserve original view  

## System Requirements

- Python 3.7+  
- PySide6  
- OpenCV (cv2)  
- NumPy  

**Notes:**
- CLAHE enhancement is optional — enable for medical images with poor contrast  
- Focus control works in real-time on processed images  
- Zoom tool works on any region of the processed image  
- All processing maintains original image quality  
- Supports Unicode file paths (Turkish characters, etc.)  

## Troubleshooting

- If images won't load, check file format compatibility  
- Ensure all dependencies are properly installed  
- Make sure your system has a proper Python environment setup before running the application  
- If you encounter issues, check that all dependencies (such as PySide6 and OpenCV) are correctly installed  




## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

**Areas for potential enhancement:**
- Additional medical imaging algorithms  
- More zoom levels and pan functionality  
- Batch processing capabilities  
- Advanced filtering options  
- Export format options  

