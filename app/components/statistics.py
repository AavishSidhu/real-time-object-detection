import streamlit as st


def initialize_statistics():

    if "images_processed" not in st.session_state:
        st.session_state.images_processed = 0

    if "videos_processed" not in st.session_state:
        st.session_state.videos_processed = 0

    if "objects_detected" not in st.session_state:
        st.session_state.objects_detected = 0


def increment_images():
    st.session_state.images_processed += 1


def increment_videos():
    st.session_state.videos_processed += 1


def add_detected_objects(count):
    st.session_state.objects_detected += count


def render_statistics():

    initialize_statistics()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📷 Images Processed",
            st.session_state.images_processed,
        )

    with col2:
        st.metric(
            "🎥 Videos Processed",
            st.session_state.videos_processed,
        )

    with col3:
        st.metric(
            "🎯 Objects Detected",
            st.session_state.objects_detected,
        )