import streamlit as st
from PIL import Image
st.set_page_config(page_title="Random Shits",layout="wide")
#asset
img_image_1 = Image.open("images/tine.jpg")

st.title("Random shits")
st.subheader("this person is not available rn.")
st.write("[The person who made this website](https://www.facebook.com/alghiejeshua.mulato.1)")

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
