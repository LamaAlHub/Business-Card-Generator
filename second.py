
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO


st.set_page_config(
    page_title="Business Card Generator",
    layout="centered"
)

st.title("Business Card Generator")

card_colors = {
    "Red": "#D64545",
    "Green": "#3A8F6B",
    "Blue": "#3B82F6",
    "Purple": "#8B5CF6"
}

color_name = st.radio(
    "Select card color",
    list(card_colors.keys()),
    horizontal=True
)

accent = card_colors[color_name]

# User information
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter your name")
    job_title = st.text_input("Enter your Job title")

with col2:
    phone = st.text_input("Enter your phone number")
    email = st.text_input("Enter your email")

# Upload image
uploaded_file = st.file_uploader(
    "Upload your profile photo or company logo",
    type=["jpg", "jpeg", "png"], accept_multiple_files=False
)


if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    # Convert uploaded image to Base64
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    encoded_image = base64.b64encode(
        buffer.getvalue()
    ).decode()


    st.subheader("Preview")
   
    
    card = Image.new(
        "RGB",
        (650, 360),
        "white"
        )


    draw = ImageDraw.Draw(card)

    # Convert HEX to RGB
    accent_rgb = tuple(
        int(accent[i:i+2], 16)
        for i in (1, 3, 5)
    )

    # Right accent
    draw.rectangle(
        (575, 0, 650, 360),
        fill=accent_rgb
    )

    # Decorative circle
    draw.ellipse(
        (500, 210, 730, 440),
        fill=accent_rgb
    )

    
    # Profile image
    profile = image.copy()

    profile = profile.resize((150, 150))
    mask = Image.new(
        "L",
        (150, 150),
        0
    )

    mask_draw = ImageDraw.Draw(mask)

    mask_draw.ellipse(
        (0, 0, 150, 150),
        fill=255
    )

    card.paste(
        profile,
        (45, 55),
        mask
    )

    # Fonts

    try:
        font_name = ImageFont.truetype(
            "arialbd.ttf",
            30
        )

        font_job = ImageFont.truetype(
            "arial.ttf",
            17
        )

        font_normal = ImageFont.truetype(
            "arial.ttf",
            14
        )

        font_brand = ImageFont.truetype(
            "arialbd.ttf",
            15
        )

    except:

        font_name = ImageFont.load_default()
        font_job = ImageFont.load_default()
        font_normal = ImageFont.load_default()
        font_brand = ImageFont.load_default()

    
    # Text
    draw.text(
        (225, 60),
        name if name else "Your Name",
        fill=(34, 34, 34),
        font=font_name
    )

    draw.text(
        (225, 105),
        job_title if job_title else "Your Job Title",
        fill=accent_rgb,
        font=font_job
    )

    draw.text(
        (225, 160),
        "Phone: " + (
            phone if phone else "000 000 0000"
        ),
        fill=(80, 80, 80),
        font=font_normal
    )

    draw.text(
        (225, 190),
        "Email: " + (
            email if email else "example@email.com"
        ),
        fill=(80, 80, 80),
        font=font_normal
    )


   
    # Convert image to bytes
    output = BytesIO()

    card.save(
        output,
        format="PNG"
    )

    png_data = output.getvalue()
    st.image(png_data, caption="Business Card Preview")

    
    # Download button
    st.download_button(
        label="Download Business Card",
        data=png_data,
        file_name="business_card.png",
        mime="image/png"
    )