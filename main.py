import streamlit as st 
import cv2 
import numpy as np 
from PIL import Image, ImageDraw, ImageFont


st.title("Business card generator")
card_color = ['red','green','blue','purple']
color = st.radio("Select card color",card_color)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter your name")
    Jobtitle = st.text_input("Enter your Job title")

with col2:
    phoneNum = st.text_input("Enter your phone number")
    email = st.text_input("Enter your email")

uploaded_file = st.file_uploader(
   "Upload your profile photo or company logo",
    type=["jpg", "png", "jpeg"],accept_multiple_files=False
)

if uploaded_file:

    IDphoto = Image.open(uploaded_file)

    st.image(IDphoto, caption="Id image")
        
    card = np.full((250,450,3),255,dtype = np.uint8)
    cvphoto = np.array(IDphoto)
    cvphoto = cv2.cvtColor(cvphoto,cv2.COLOR_RGB2BGR)
    cvphoto = cv2.resize(cvphoto,(160,160))
    card[20:180 , 20:180]= cvphoto
    
    if color == 'blue':
        card = cv2.rectangle(card,(400,0),(450,250),(139, 0, 0),-1)
        card = cv2.putText(card,name,(185,40),cv2.FONT_HERSHEY_TRIPLEX,1,(139, 0, 0),1)
    elif color == 'red':
        card = cv2.rectangle(card,(400,0),(450,250),(0, 0, 139),-1)
        card = cv2.putText(card,name,(185,40),cv2.FONT_HERSHEY_TRIPLEX,1,(0, 0, 139),1)
    elif color == 'green':
        card = cv2.rectangle(card,(400,0),(450,250),(0, 139, 0),-1)
        card = cv2.putText(card,name,(185,40),cv2.FONT_HERSHEY_TRIPLEX,1,(0, 139, 0),1)
    elif color == 'purple':
        card = cv2.rectangle(card,(400,0),(450,250),(128, 0, 128),-1)
        card = cv2.putText(card,name,(185,40),cv2.FONT_HERSHEY_TRIPLEX,1,(128, 0, 128),1)

    card = cv2.putText(card,Jobtitle,(185,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    card = cv2.putText(card,"phone number: "+ phoneNum,(185,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    card = cv2.putText(card,"email: "+ email,(185,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
   
    card_pil = Image.fromarray(cv2.cvtColor(card, cv2.COLOR_BGR2RGB))

    draw = ImageDraw.Draw(card_pil)
    st.image(card_pil,caption="Business card")
    success = cv2.imwrite("business_card.png", card)
    if success:
        with open("business_card.png", "rb") as file:
            btn = st.download_button(
                label="Download Business Card",
                data=file,
                file_name="business_card.png",
                mime="image/png"
            )
    else:
        st.error("Failed to save the business card image.")