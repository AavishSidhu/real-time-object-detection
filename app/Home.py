import streamlit as st

from app.components.sidebar import render_sidebar


st.set_page_config(
    page_title="AI Vision Suite",
    page_icon="🎯",
    layout="wide",
)

render_sidebar()

st.title("🎯 AI Vision Suite")

st.markdown(
    """
### Real-Time Object Detection Platform

Detect and analyze objects using **YOLOv8** across multiple input sources.

Built with **Python**, **YOLOv8**, **OpenCV**, and **Streamlit**.
"""
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
### 🖼️ Image Detection

Upload images and detect objects instantly.
"""
    )

with col2:
    st.info(
        """
### 🎥 Video Detection

Analyze complete videos frame-by-frame.
"""
    )

with col3:
    st.info(
        """
### 📷 Webcam Detection

Run live real-time object detection.
"""
    )

st.divider()

st.subheader("✨ Features")

st.markdown("""
- ✅ YOLOv8 Object Detection
- ✅ Image Upload
- ✅ Video Processing
- ✅ Live Webcam Detection
- ✅ Confidence Threshold Adjustment
- ✅ Object Counting
- ✅ FPS Monitoring
- ✅ Modern Dashboard
""")

st.divider()

st.caption("Version 1.0 • Built by Aavish Sidhu")