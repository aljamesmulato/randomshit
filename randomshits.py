import streamlit as st
from PIL import Image
st.set_page_config(page_title="Happy Birthday",layout="wide")
#asset
img_image_1 = Image.open("images/tine.jpg")

st.title("Happy Birthday")
st.write("[Click this link this is not a virus](https://youtu.be/ykHAwUhjjGE?si=FbltIc_DAe36oGfk)")

with st.container():
    st.write("---")
    left_1, image_1 = st.columns((1,1))
    with left_1:
        st.header("Happy 17th Birthday")
        st.write("##")
        st.write(
            """
            Happy birthday to you wish u all the best and more birthdays to come!:birthday_cake::shortcake:
            :confetti_ball:

            """
        

        )
    with image_1:
        st.image(img_image_1)
