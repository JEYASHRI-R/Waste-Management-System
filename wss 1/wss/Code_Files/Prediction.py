import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image
import os

UPLOADED_FILES = r"C:/....................../Images"
waste_segregation_model = tf.keras.models.load_model(r'C:/.................segration_predict.h5')

st.markdown("<h3 style='text-align: center; color: rgb(227, 38, 54);'>AI Powered Waste Segregator</h3>", unsafe_allow_html=True)
uploaded_files = st.file_uploader("Supported format: jpg, png", accept_multiple_files=True)

if uploaded_files:
    process_button = st.button("Upload")
    if process_button:
        for uploaded_file in uploaded_files:
            try:
                img = Image.open(uploaded_file)
                
                img_path = os.path.join(UPLOADED_FILES, uploaded_file.name)
                img.save(img_path)

                bio = [0, 3]
                nonbio = [1, 2, 4]
                img = load_img(img_path, target_size=(64, 64))
                x = img_to_array(img)
                x = np.expand_dims(x, axis=0)
                pred = np.argmax(waste_segregation_model.predict(x))
                   
                col1, col2 = st.columns([3,1]) 
                with col1:
                    st.image(img, caption="Uploaded Image", use_column_width=True)
                with col2:
                    if pred in bio:
                        st.write("Waste Type: Bio-Degradable Waste")
                        if pred == 0:
                            st.write("Waste Classified as: Food Waste")
                        elif pred == 3:
                            st.write("Waste Classified as: Paper Waste")
                    else:
                        st.write("Waste Type: Non Bio-Degradable Waste")
                        if pred == 1:
                            st.write("Waste Classified as: Glass Waste")
                        elif pred == 2:
                            st.write("Waste Classified as: Metal Waste")
                        elif pred == 4:
                            st.write("Waste Classified as: Plastic Waste")

            except Exception as e:
                st.write(f"Error processing {uploaded_file.name}: {e}")
