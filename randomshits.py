import streamlit as st
from PIL import Image
st.set_page_config(page_title="Random Shits",layout="wide")
#asset
img_image_1 = Image.open("images/alghie.jpg")

st.title("Random shits")
st.subheader("this person is not available rn.")
st.write("[The person who made this website](https://www.facebook.com/alghiejeshua.mulato.1)")

with st.container():
    st.write("---")
    left_1, image_1 = st.columns((1,1))
    with left_1:
        st.header("Hi, I'm Alghie")
        st.write("##")
        st.write(
            """
            This is the person who made this link
            This guy is the most sweet person and kind person
            gives u good vibes as always, u can always trust him


            """
        

        )
    with image_1:
        st.image(img_image_1)

#asset
img_image_2 = Image.open("images/pusa.jpg")

with st.container():
    st.write("---")
    image_2, left_1 = st.columns((1,15))
    with left_1:
        st.header("my favourite pet is cat")
        st.write("##")
        st.write(
            """
            the reason why i love cats its because they're so cute and fluffy

            """


        )
    with image_2:
        st.image(img_image_2)

