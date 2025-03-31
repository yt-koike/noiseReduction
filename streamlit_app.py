import cv2
from PIL import Image
import numpy as np
import streamlit as st

def pil2cv(image):
    new_image = np.array(image, dtype=np.uint8)
    new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    return new_image

def cv2pil(image):
    new_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return new_image

st.title("ノイズ除去 Web アプリ")

filepath = st.file_uploader(
    "画像をアップロードしてください.", type=["jpg", "jpeg", "png"], key=1
)

k = st.number_input("Kernel Size(多くするほど ぼやけが強い)",value=5,step=2)
ite = st.number_input("Iteration(フィルタをかける回数)",value=1)
gau1 = st.number_input("G1",value=20)
gau2 = st.number_input("G2",value=20)

if filepath is not None:
    if k is not None:
        kernelSize = int(k)
    if ite is not None:
        iterationN = int(ite)
    st.write("Original")
    st.image(filepath)
    
    img = pil2cv(Image.open(filepath))
    aveImg = img.copy()
    gauImg = img.copy()
    bilatImg = img.copy()
    for _ in range(iterationN):
        aveImg = (cv2.blur(aveImg, (kernelSize, kernelSize)))
        gauImg = (cv2.GaussianBlur(gauImg, (kernelSize, kernelSize), int(gau1)))
        bilatImg = cv2.bilateralFilter(bilatImg,kernelSize, int(gau1), int(gau2))
    st.write("Average")
    st.image(cv2pil(aveImg))
    st.write("Gaussian")
    st.image(cv2pil(gauImg))
    st.write("Bilateral")
    st.image(cv2pil(bilatImg))
