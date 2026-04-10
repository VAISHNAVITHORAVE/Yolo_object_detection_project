import streamlit as st
from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image

# Load YOLO model
model = YOLO("runs/detect/Construction_Safety_Final/weights/best.pt")

# Title
st.title("🚧 Construction Safety Detection System")
st.write("Upload an image to detect helmet, vest, and person")

# File uploader (IMPORTANT)
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# Check if file uploaded
if uploaded_file is not None:

    # Convert image to RGB (FIX previous error)
    image = Image.open(uploaded_file).convert("RGB")

    # Show uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert to numpy
    img = np.array(image)

    # Prediction
    results = model.predict(source=img)

    # Get output image
    output = results[0].plot()

    # Convert BGR to RGB
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

    # Show result
    st.image(output, caption="Detection Result", use_container_width=True)

    st.success("✅ Detection Completed")