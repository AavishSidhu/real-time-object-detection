import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🎯 Object Detection")

        st.markdown("---")

        st.markdown(
            """
### Tech Stack

- YOLOv8
- OpenCV
- Streamlit
- Python
"""
        )

        st.markdown("---")

        st.info(
            "Detect objects in images, videos, and live webcam streams."
        )

        st.markdown("---")

        st.caption("Version 1.0")