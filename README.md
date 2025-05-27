### _**Medical Image Processor with Interactive Zoom**_


🧠 **Project Description**

This project is a medical image processing application developed using PySide6 and OpenCV, as part of the Computational Methods in Engineering course at Ankara University, Department of Biomedical Engineering.
It provides an interactive GUI for real-time image operations, including grayscale conversion, edge detection, dynamic zooming with mouse wheel, and magnification through mouse click.

✨ **Features**

**Image Upload:** Load PNG, JPEG, and JPG images through a user-friendly file dialog.  

**Grayscale Conversion:** Convert colored medical images to grayscale. Brightness can be adjusted dynamically via a slider.  

**Edge Detection:** Apply Canny edge detection with real-time control over low and high threshold values using sliders.

**Brightness Control:** Fine-tune image brightness to improve visibility and contrast during preprocessing.  

**Interactive Zoom:**  Scroll the mouse wheel to adjust image sharpness (simulate focus by clarifying or blurring the image).  

Use the zoom area slider to set the zoom level. 

Select the region to zoom into for focused inspection.  

Left-click on the image to activate the magnifier tool and view pixel-level detail, even after zooming. 

**Image Saving:** Save the processed image in PNG or JPEG format with a single click.



**Installation**

Clone the repository: bash git clone https://github.com/ecebuketgokcen/Medical-Image-Processor-with-Interactive-Zoom.git

cd Medical-Image-Processor-with-Interactive-Zoom


Install dependencies: bash pip install -r requirements.txt 

install manually: bash pip install PySide6 opencv-python


**Usage**

Run the application using: bash python main.py

Once the GUI opens:

Click Load Image to select an image from your computer.

Use the Grayscale or Edge Detection buttons to apply filters.

Scroll the mouse wheel to adjust the sharpness (simulate focus by clarifying or blurring the image).

Move the slider to set the zoom level, and select the region you want to zoom into.

Left-click on the image to activate the magnifier tool.

Click Save Image to export the processed version.




**Screenshots**

**Main Window**

![Image](https://github.com/user-attachments/assets/91ef679d-b1fa-4561-bd80-44fca1ffb628)


**Grayscale** 

![Image](https://github.com/user-attachments/assets/1f33e9e7-5163-4aab-8491-f9eb9b800b35)

![Image](https://github.com/user-attachments/assets/5c68f75b-b7be-4950-8dbe-697ee38d7b8b)


**Edge Detection**

![Image](https://github.com/user-attachments/assets/d19da331-674b-45fe-82cd-04f915c5b21f)


**Zoomed Region**

![Image](https://github.com/user-attachments/assets/1749099d-5267-4b3f-9a24-2d9ad13f8a87)

![Image](https://github.com/user-attachments/assets/ab01d866-bff2-4fb4-b8b2-ff172c413e56)

![Image](https://github.com/user-attachments/assets/1aefeeb7-e94b-41fd-9662-103d48d6ceef)



📝 **Notes**

Ensure your system has a proper Python environment setup before running the application. If you encounter issues, check that all dependencies (such as PySide6 and OpenCV) are correctly installed.


**Contributing**

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
