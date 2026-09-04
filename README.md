# Business Card Generator

A simple and customizable Business Card Generator built with Python and Streamlit.

The application allows users to enter their business and personal information, upload a profile image, choose a card color, preview the card, and download the final design as a PNG image.


## 🛠️ Technologies Used

- Python
- Streamlit
- OpenCV
- Pillow (PIL)
- NumPy

## 📂 Project Versions

This project contains two versions of the Business Card Generator.

### Version 1 — OpenCV

The first version was developed using OpenCV.

OpenCV was used to:
- Create the card background
- Draw shapes and elements
- Resize and process images
- Add text to the card

However, while OpenCV works very well for image processing and computer vision tasks, designing a clean and modern business card with custom fonts, spacing, rounded elements, and other UI-style details was more challenging.

### Version 2 — Pillow

To make the card design easier to control and more visually organized, I moved to Pillow.

Pillow made it easier to:
- Work with custom fonts
- Position text accurately
- Resize and manipulate images
- Design the card layout

The second version is therefore the improved version of the project and is the recommended version to use.

## 📁 Project Structure

```text
business-card-generator/
│
├── app.py
├── requirements.txt
├── README.md
│
└── assets/
    └── ...
