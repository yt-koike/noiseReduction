import cv2
import streamlit as st

st.title("画像類似度比較 Web アプリ")

filepath = st.file_uploader(
    "画像をアップロードしてください.", type=["jpg", "jpeg", "png"], key=1
)

if filepath is not None:
    st.write("Original")
    st.image([filepath], width=300)

    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    aveImg = cv2.blur(img, (5, 5))
    gauImg = cv2.GaussianBlur(img, (5, 5), 20)
    bilatImg = cv2.bilateralFilter(img, 5, 20, 20)
    st.image([aveImg, gauImg, bilatImg], width=300)
