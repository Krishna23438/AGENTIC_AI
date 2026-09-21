import streamlit as st

from youtube_analyzer import youtube_agent


st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered"
)

st.title("🎥 AI YouTube Video Analyzer")


@st.cache_resource
def get_agent():
    return youtube_agent()


agent = get_agent()

if agent is None:
    st.error("Agent initialization failed.")
    st.stop()


video_url = st.text_input("Enter YouTube URL")# String

button = st.button("Analyze Video")# Boolean - True or false


if video_url and button:
    with st.spinner("Analyzing video..."):

        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("## Analysis Report of Video")

    st.markdown(response.content)