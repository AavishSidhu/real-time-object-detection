import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

import tempfile

import cv2
import streamlit as st

from src.detection.model import load_model
from src.detection.predict import detect_image
from app.components.sidebar import render_sidebar
from app.components.statistics import (
    render_statistics,
    increment_images,
    add_detected_objects,
)
st.set_page_config(
    page_title="Image Detection",
    page_icon="🖼️",
    layout="wide",
)


@st.cache_resource
def get_model():
    return load_model()


model = get_model()
render_sidebar()
render_statistics()

st.title("🖼️ Image Detection")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
)

confidence = st.slider(
    "Confidence Threshold",
    min_value=0.10,
    max_value=1.00,
    value=0.50,
    step=0.05,
)


if uploaded_file is not None:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(uploaded_file, use_container_width=True)

    if st.button("Detect Objects"):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name

        annotated_image, results = detect_image(
            model=model,
            image_path=temp_path,
            confidence=confidence,
        )
        increment_images()
        add_detected_objects(len(results[0].boxes))

        annotated_image = cv2.cvtColor(
            annotated_image,
            cv2.COLOR_BGR2RGB,
        )

        with col2:
            st.subheader("Detection Result")
            st.image(
                annotated_image,
                use_container_width=True,
            )

        st.subheader("Detected Objects")

        if len(results[0].boxes) == 0:
            st.warning("No objects detected.")

        else:
            for box in results[0].boxes:
                class_id = int(box.cls)
                confidence_score = float(box.conf)
                class_name = model.names[class_id]

                st.write(
                    f"**{class_name}** — {confidence_score:.2f}"
                )