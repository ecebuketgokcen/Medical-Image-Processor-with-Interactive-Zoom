### _**Medical Image Processor with Interactive Zoom**_


[🧠 **Project Description**](url)

Medical Image Processor with Interactive Zoom is a Python-based GUI application developed using PySide 6 and OpenCV. It allows users to perform basic image processing tasks such as grayscale conversion and edge detection on medical images. The application features two forms of visual inspection: users can scroll the mouse wheel to adjust image sharpness (simulate focus), and they can zoom into a selected region by adjusting the zoom area slider and choosing the desired part of the image. A magnifier tool activated by left-click further enhances detailed analysis of specific areas.

This project was developed as part of the Computational Methods in Engineering course at Ankara University, Department of Biomedical Engineering.

[✨ **Features**](url)

**Image Upload:** Load PNG, JPEG, and JPG images through a user-friendly file dialog.  

**Grayscale Conversion:** Convert colored medical images to grayscale. Brightness can be adjusted dynamically via a slider.  

**Edge Detection:** Apply Canny edge detection with real-time control over low and high threshold values using sliders.

**Brightness Control:** Fine-tune image brightness to improve visibility and contrast during preprocessing.  

**Interactive Zoom:**  Scroll the mouse wheel to adjust image sharpness (simulate focus by clarifying or blurring the image).  

Use the zoom area slider to set the zoom level. 

Select the region to zoom into for focused inspection.  

Left-click on the image to activate the magnifier tool and view pixel-level detail, even after zooming. 

**Image Saving:** Save the processed image in PNG or JPEG format with a single click.


[**Installation**](url)

Clone the repository: bash git clone `https://github.com/ecebuketgokcen/Medical-Image-Processor-with-Interactive-Zoom.git `

`cd Medical-Image-Processor-with-Interactive-Zoom`

Install dependencies: bash `pip install -r requirements.txt `

install manually: bash `pip install PySide6 opencv-python`

[**Usage**](url)

Run the application using: bash `python main.py`

Once the GUI opens:

Click Load Image to select an image from your computer.

Use the Grayscale or Edge Detection buttons to apply filters.

Scroll the mouse wheel to adjust the sharpness (simulate focus by clarifying or blurring the image).

Move the slider to set the zoom level, and select the region you want to zoom into.

Left-click on the image to activate the magnifier tool.

Click Save Image to export the processed version.




[**Screenshots**](url)

**Main Window**

![imageprocessor](https://github.com/user-attachments/assets/9410813f-69ce-4b49-80b0-3fe5b98654ef)

**Grayscale** 

![grayscale2](https://github.com/user-attachments/assets/a1dc5d36-3c45-4552-8b06-a43b77c9d005)
![grayscale1](https://github.com/user-attachments/assets/5239c2cb-7ffc-4564-ab94-bfc8832b8b90)

**Edge Detection**

![edge detection1](https://github.com/user-attachments/assets/7a257ebf-c1e1-4b26-9b03-cd750be37aa4)


**Zoomed Region**

![zoom3](https://github.com/user-attachments/assets/5e3ef3e1-6716-437b-968b-cee13edcb32f)
![zoom2](https://github.com/user-attachments/assets/5c8be795-7d6d-4981-addd-428a7b5cde83)
![zoom1](https://github.com/user-attachments/assets/0a3e6af3-5b19-4d78-9920-cdbc33e2f346)



[📝**Notes**](url)

Ensure your system has a proper Python environment setup before running the application. If you encounter issues, check that all dependencies (such as PySide6 and OpenCV) are correctly installed.



[**Contributing**](url)

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

