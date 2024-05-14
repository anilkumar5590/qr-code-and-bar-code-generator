# Hi, I'm Anil Kumar! 👋

## QR Code and Bar Code Generator
This Streamlit application allows users to generate QR codes and Bar codes with customizable options.

## Features
- `QR Code Generation`: Users can input content and select fill and background colors to generate QR codes.
- `Bar Code Generation`: Users can choose from EAN-13, Code 128, or ISBN-13 formats to create bar codes.
- `Download Functionality`: Generated QR codes and Bar codes can be downloaded as PNG images.

## How to Use
1. Select Code Type:
- Open the application and select whether you want to generate a QR Code or Bar Code by clicking on the respective option.
2. Generate QR Code:
- If you selected QR Code, enter the desired content (e.g., text, URL) into the input field provided.
- Choose the fill and background colors for the QR Code using the color pickers.
- Click on the "Download QR Code" button to save the generated QR Code as a PNG image.
3. Generate Bar Code:
- If you selected Bar Code, choose the type of barcode you want to generate (EAN-13, Code 128, or ISBN-13) from the dropdown menu.
- Enter the content (e.g., numbers, alphanumeric code) into the input field provided.
- Click on the "Download Bar Code" button to save the generated Bar Code as a PNG image.

## Installation

Install the required packages:
```bash
pip install -r requirements.txt
```
or
```bash
pip install streamlit streamlit_option_menu qrcode pillow python-barcode
```

## Running the Application
Run the Streamlit application:
```bash
streamlit run generator.py
```

## Dependencies
- `Streamlit`: A web application framework for Python. It allows you to create interactive web applications directly from Python scripts.
- `streamlit_option_menu`: A Streamlit component that enhances the user interface by providing dropdown menus with icons and customization options.
- `qrcode`: A Python library that generates QR codes. It supports various customization options such as error correction level, size, and color.
- `Pillow (PIL)`: A Python imaging library used for image processing. It is used in this application to save the generated QR codes and Bar codes as PNG images.
- `python-barcode`: A library for generating various types of barcodes, including EAN-13, Code 128, and ISBN-13. It provides functionalities to create barcode images with customizable options.


## Use Cases:
- `Businesses`: Use QR codes for marketing campaigns, product information, and contact details. Barcodes can be used for product labeling and inventory management.
- `Educators`: Generate QR codes for sharing resources, links to online content, and interactive activities. Barcodes can be used in educational materials and assessments.
- `Retailers`: Create barcodes for product labels, pricing, and tracking inventory. QR codes can be used for promotions, loyalty programs, and mobile payments.

## Contributing
Contributions to enhance and improve this application are welcome! If you have suggestions, bug fixes, or new features, feel free to submit a pull request.


## Preview
[Checkout Here]()

## 🔗 Follow us
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anilkumarkonathala/)

## Feedback
If you have any feedback, please reach out to us at konathalaanilkumar143@gmail.com