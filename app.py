import base64
import time
import constants
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image


model = tf.keras.models.load_model(constants.MODEl_PATH)


def predict_class(image_path):
    original_image = Image.open(image_path)

    preprocessed_image = original_image.resize((256, 256))
    preprocessed_image = np.array(preprocessed_image) / 255.0

    preds = model.predict(np.expand_dims(preprocessed_image, axis = 0))
    labels = ['Healthy', 'Powdery', 'Rust']

    preds_class = np.argmax(preds)
    preds_label = labels[preds_class]

    return preds_label, round(preds[0][preds_class], 2)

################## STREAMLIT APP ##################

@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s") !important;
    background-size: cover !important;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('assets/bg.png')

st.write("<h1>Plant Disease Detection using CNN</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.image("assets/logo.png")
    
    uploaded_file = st.file_uploader("Upload an image", type = ['png', 'jpg', 'jpeg'])
    
    st.info("""
            # About
            This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).
            
            # Contact
            For inquiries, you can mail us [here](mailto:arpitsengar99@gmail.com).
            """)

home_page = st.empty()
home_page.write(constants.FRONT_PAGE, unsafe_allow_html=True)

display_image = st.empty()
classifying_text = st.empty()
button = st.empty()    

# use_sample_image = st.checkbox("Use example image", value = False)

# if use_sample_image:
#     display_image.image(f'sample/{random.randint(1,10)}.jpg')
#     uploaded_file = True


if uploaded_file is not None:
    home_page.empty()
    display_image.image(uploaded_file)
    
    predict_button = button.button("Predict", use_container_width=True)

    if predict_button and uploaded_file is not None: 
        classifying_text.empty()
        button.empty()
        label, confidence = predict_class(uploaded_file)
        
        loading_bar = st.empty()
        loading_bar.write("Classifying...")
        progress_text = "Please wait, we're predicting the image..."
        my_bar = loading_bar.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)

        my_bar.empty()
        st.toast("Prediction Complete!")
        st.info(f"##### Prediction: {label}\n##### Confidence: {confidence}")

    classifying_text.empty()