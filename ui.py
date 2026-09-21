import streamlit as st
from youtube_analyzer import youtube_agent


st.set_page_config(
  page_title="Youtube Video Analyzer",
  layout='centered'
)

st.title("🎥 AI Youtube Video Analyzer")

def get_agent():
   return youtube_agent()