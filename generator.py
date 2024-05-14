import streamlit as st
from streamlit_option_menu import option_menu
import qrcode
from PIL import Image
import io
from random import randint
import barcode
from barcode.writer import ImageWriter

# Create a dropdown menu with options for QR Code and Bar Code
selected_option=option_menu("Generator",["QR Code","Bar Code"],icons=["genie","camera_with_flash"],orientation="horizontal")

# Define a QR code generator function
qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
def qrcode_generator(qr_content,fillColor,backColor):
        # Add the data to the QR code
        qr.add_data(qr_content)
        qr.make(fit=True)

        # Generate the QR code image
        qr_img = qr.make_image(fill_color=fillColor, back_color=backColor)

        # Convert the image to bytes
        img_bytes = io.BytesIO()
        qr_img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()

        # Return the QR code image bytes
        return img_bytes

# Define a function to generate a random output filename for QR codes
def qrOutputFilename():
        output_name="qrcode-"
        for i in range(5):
            k=str(randint(1,9))
            output_name+=k
        
        output_name+=".png"
        return output_name

# Define a function to generate a random output filename for barcodes
def barOutputFilename():
    output_name="barcode-"
    for i in range(5):
        k=str(randint(1,9))
        output_name+=k
        
    output_name+=".png"
    return output_name

# Define a barcode generator function
def barcode_generator(barcode_type, data):
    # Create a barcode object
    barcode_object = barcode.get_barcode_class(barcode_type)(data, writer=ImageWriter())

    # Generate the barcode image
    img_bytes = io.BytesIO()
    barcode_object.write(img_bytes)
    img_bytes.seek(0)

    # Return the barcode image bytes
    return img_bytes.getvalue()

# Main program
if selected_option=="QR Code":
    # Get the QR code content from the user
    qr_content = st.text_input("Enter the conent here",placeholder="Type the content or paste the url here ...",label_visibility="hidden")

    # Check if the user entered any content
    if qr_content:
        # Create a column for the fill color selection
        t1,t2=st.columns(2)
        with t1:
            fillColorSelection=st.color_picker('Select the Fill Color',value="#000")
        with t2:
            backColorSelection=st.color_picker('Select the Back Color',value="#fff")

        # Generate the QR code image
        qrgenerated_image=qrcode_generator(qr_content,fillColorSelection,backColorSelection)

        # Display the QR code image
        st.image(qrgenerated_image, caption="QR Code Generated", width=300)

        # Generate a random output filename for the QR code
        qrOutput=qrOutputFilename()

        # Create a column for the download button
        col1,col2=st.columns(2)  
        with col2:
            # Create a download button for the QR code
            st.download_button(
            label="Download QR Code",
            data=qrgenerated_image,
            file_name=qrOutput,
        )
            
elif selected_option=="Bar Code":
    # Get the bar code type from the user
    bar_type=st.selectbox("Select Bar Code type",["EAN13", "Code128", "ISBN13"])

    # Display information about the bar code types
    st.write("The EAN-13 format should contain 13 digits in total.")
    st.write("The Code 128 format should contain all 128 ASCII code characters, including numbers, upper case and lower case letters, symbols, and control codes.")
    st.write("The ISBN-13 consists of 13 digits and Prefix element (usually 978 or 979)")

    # Get the bar code content from the user
    bar_content=st.text_input("Enter the content here",placeholder="Type the number content here ...",value=None,label_visibility="hidden")

    # Check if the user entered any content
    try:
        if bar_content:
            # Generate the bar code image
            bargenerated_image=barcode_generator(bar_type,bar_content)

            # Generate a random output filename for the bar code
            barOutput=barOutputFilename()

            # Display the bar code image
            st.image(bargenerated_image, caption="Bar Code Generated", width=300)

            # Create a column for the download button
            col1,col2=st.columns(2)
            with col2:
                # Create a download button for the bar code
                st.download_button(
                label="Download Bar Code",
                data=bargenerated_image,
                file_name=barOutput,
            )
        
    except:
         pass