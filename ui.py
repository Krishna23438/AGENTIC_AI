import streamlit as st
from youtube_analyzer import youtube_agent


st.set_page_config(
  page_title="Youtube Video Analyzer",
  layout='centered'
)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
   return youtube_agent()

agent = get_agent()

# input box
video_url = st.text_input("Enter Youtube URL") # string

button = st.button("Analyze Video") # BOOL - True or false

if video_url and button:
   with st.spinner("analyzing video..."):
      response = agent.print_response(
         f"Analyze this video: {video_url}"
      )

   print(response)