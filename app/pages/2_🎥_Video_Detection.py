import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

import tempfile
import uuid

import streamlit as st

from src.detection.model import load_model
from src.detection.video import process_video
from app.components.sidebar import render_sidebar
from app.components.statistics import render_statistics

st.set_page_config(
    page_title="Video Detection",
    page_icon="🎥",
    layout="wide",
)


@st.cache_resource
def get_model():
    return load_model()


model = get_model()
render_sidebar()
render_statistics(
    images=128,
    videos=19,
    objects=5942,
)

st.title("🎥 Video Detection")

uploaded_video = st.file_uploader(
    "Upload a video",
    type=["mp4", "avi", "mov"],
)

confidence = st.slider(
    "Confidence Threshold",
    min_value=0.10,
    max_value=1.00,
    value=0.50,
    step=0.05,
)


if uploaded_video is not None:

    if st.button("Process Video"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4",
        ) as input_file:

            input_file.write(uploaded_video.read())
            input_path = input_file.name

        output_path = f"data/outputs/{uuid.uuid4()}.mp4"

        with st.spinner("Processing video..."):

            process_video(
                model=model,
                input_path=input_path,
                output_path=output_path,
                confidence=confidence,
            )

        st.success("Video processed successfully!")

        with open(output_path, "rb") as video_file:
            video_bytes = video_file.read()

        st.video(video_bytes)