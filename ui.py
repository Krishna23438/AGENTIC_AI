from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
import re
import streamlit as st
from youtube_analyzer import youtube_agent

def create_pdf(content):
    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=20,
        leading=24,
        spaceAfter=15,
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15,
        alignment=TA_LEFT,
        spaceAfter=8,
    )

    story = []

    story.append(
        Paragraph(
            "🎥 AI YouTube Video Analysis Report",
            title_style
        )
    )

    story.append(Spacer(1, 10))

    # Convert content into separate paragraphs
    for line in content.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 6))
            continue

        # Basic Markdown cleanup
        line = line.replace("**", "")
        line = line.replace("__", "")

        # Escape characters that ReportLab interprets as HTML
        line = (
            line.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
        )

        story.append(
            Paragraph(line, body_style)
        )

    doc.build(story)

    pdf_buffer.seek(0)

    return pdf_buffer.getvalue()

st.set_page_config(
    page_title="AI YouTube Video Analyzer",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Styling ----------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(1200px 600px at 10% -10%, #2a0d12 0%, #0f0f0f 45%, #0a0a0a 100%);
    color: #f1f1f1;
}
#MainMenu, footer, header {visibility: hidden;}

.hero {
    padding: 2.2rem 2.4rem;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(255,0,51,.18), rgba(255,255,255,.03));
    border: 1px solid rgba(255,255,255,.08);
    box-shadow: 0 20px 60px -25px rgba(255,0,51,.5);
    margin-bottom: 1.6rem;
}
.hero h1 {
    font-size: 2.6rem; font-weight: 800; margin: 0;
    background: linear-gradient(90deg, #fff 20%, #ff4d6d 90%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero p { color: #b3b3b3; font-size: 1.02rem; margin-top: .5rem; }

.card {
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    backdrop-filter: blur(8px);
}

.pill {
    display:inline-block; padding:.28rem .8rem; margin-right:.4rem;
    font-size:.75rem; letter-spacing:.04em; text-transform:uppercase;
    border-radius:999px; background:rgba(255,0,51,.15);
    border:1px solid rgba(255,0,51,.35); color:#ff8095;
}

div.stTextInput > div > div > input {
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 14px; color: #fff; padding: .85rem 1rem; font-size: 1rem;
}
div.stTextInput > div > div > input:focus {
    border-color: #ff0033; 
    color:#000000;
    box-shadow: 0 0 0 3px rgba(255,0,51,.25);
}

div.stButton > button {
    width: 100%; border: none; border-radius: 14px;
    padding: .8rem 1.2rem; font-weight: 700; font-size: 1rem;
    color: #ffffff; background: linear-gradient(135deg, #ff0033, #ff5c36);
    box-shadow: 0 12px 30px -12px rgba(255,0,51,.8);
    transition: transform .15s ease, box-shadow .15s ease;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    background: #8c0412;
    box-shadow: 0 18px 40px -12px rgba(255,0,51,.95);
}

/* Download report button */
.stDownloadButton > button {
    background: #8a0634 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.4rem !important;
    font-weight: 600 !important;
}
.stDownloadButton > button:hover {
    background: #ad0919 !important;
}



.stTabs [data-baseweb="tab-list"] { gap: .5rem; border-bottom: 1px solid rgba(255,255,255,.08); }
.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,.04); border-radius: 12px 12px 0 0;
    padding: .6rem 1.2rem; color: #b3b3b3;
}
.stTabs [aria-selected="true"] { background: rgba(255,0,51,.18) !important; color:#fff !important; }

.report h1,.report h2,.report h3 { color:#fff; }
.report { line-height: 1.75; font-size: 1.02rem; }
</style>
""", unsafe_allow_html=True)


def extract_video_id(url: str):
    patterns = [
        r"(?:v=|\/embed\/|\.be\/|\/shorts\/)([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url or "")
        if m:
            return m.group(1)
    return None


@st.cache_resource
def get_agent():
    return youtube_agent()


agent = get_agent()

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("### ⚙️ Analyzer")
    st.markdown(
        '<div class="card">Paste any YouTube link — video, Shorts or youtu.be — '
        'and the agent will summarize, extract key points and give insights.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.caption("Status")
    if agent is None:
        st.error("Agent offline")
    else:
        st.success("Agent ready")
    if st.session_state.get("history"):
        st.markdown("### 🕘 Recent")
        for item in reversed(st.session_state["history"][-5:]):
            st.markdown(f"- `{item}`")

# ---------- Hero ----------
st.markdown("""
<div class="hero">
  <span class="pill">Agentic AI</span><span class="pill">Video Intelligence</span>
  <h1>🎥 AI YouTube Video Analyzer</h1>
  <p>Turn any YouTube video into a structured, readable report — summary, key takeaways and insights in seconds.</p>
</div>
""", unsafe_allow_html=True)

if agent is None:
    st.error("Agent initialization failed. Check your API keys and try again.")
    st.stop()

st.session_state.setdefault("history", [])

col_input, col_btn = st.columns([4, 1], vertical_alignment="bottom")
with col_input:
    video_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed",
    )
with col_btn:
    analyze = st.button("🚀 Analyze")

vid = extract_video_id(video_url)

if video_url and not vid:
    st.warning("That doesn't look like a valid YouTube link.")

if analyze and vid:
    left, right = st.columns([1.1, 1.6], gap="large")

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(f"https://img.youtube.com/vi/{vid}/maxresdefault.jpg",
                 use_container_width=True)
        st.markdown(f"**Video ID:** `{vid}`")
        st.link_button("Open on YouTube", video_url, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        with st.spinner("🤖 Agent is watching and analyzing the video..."):
            try:
                response = agent.run(f"Analyze this video: {video_url}")
                content = getattr(response, "content", str(response))
            except Exception as e:
                content = None
                st.error(f"Analysis failed: {e}")

        if content:
          st.session_state["history"].append(vid)
      
          tab_report, tab_raw = st.tabs(
              ["📊 Report", "🧾 Raw output"]
          )
      
          with tab_report:
      
              st.markdown(
                  f'<div class="card report">      {content}</div>',
                  unsafe_allow_html=True
              )
      
              # Create PDF
              pdf_data = create_pdf(content)
      
              st.download_button(
                  "⬇️ Download PDF Report",
                  data=pdf_data,
                  file_name=f"analysis_{vid}.pdf",
                  mime="application/pdf",
                  use_container_width=True,
              )
      
          with tab_raw:
      
              st.code(
                  content,
                  language="markdown"
              )
elif not analyze:
    st.markdown("""
<div class="card">
  <b>How it works</b><br><br>
  1️⃣ Paste a YouTube URL above &nbsp;•&nbsp; 2️⃣ Hit <b>Analyze</b> &nbsp;•&nbsp; 3️⃣ Read or download your report
</div>
""", unsafe_allow_html=True)
