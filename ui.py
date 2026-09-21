
import streamlit as st
from youtube_analyzer import youtube_agent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="YouTube AI Analyzer",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- Global ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(255, 0, 80, 0.08),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(80, 80, 255, 0.08),
                transparent 30%
            ),
            #0b0f19;
    }

    .main {
        padding-top: 1rem;
    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"] {
        background: #080c14;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    .sidebar-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .sidebar-text {
        color: #9ca3af;
        font-size: 14px;
        line-height: 1.6;
    }

    .feature-card {
        padding: 14px;
        margin: 10px 0;
        border-radius: 12px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.07);
    }

    /* ---------- Hero ---------- */

    .hero {
        text-align: center;
        padding: 45px 20px 25px 20px;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 30px;
        background: rgba(255, 0, 80, 0.12);
        border: 1px solid rgba(255, 0, 80, 0.25);
        color: #ff4d78;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 52px;
        font-weight: 800;
        letter-spacing: -2px;
        margin-bottom: 10px;
        background: linear-gradient(
            90deg,
            #ffffff,
            #ff4d78,
            #8b7cff
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        max-width: 700px;
        margin: auto;
        color: #aab1c0;
        font-size: 18px;
        line-height: 1.6;
    }

    /* ---------- Analyzer Card ---------- */

    .analyzer-card {
        max-width: 900px;
        margin: 25px auto;
        padding: 28px;
        border-radius: 20px;
        background: rgba(255,255,255,0.045);
        border: 1px solid rgba(255,255,255,0.09);
        box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    }

    .section-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .section-subtitle {
        color: #8f98a8;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* ---------- Input ---------- */

    div[data-testid="stTextInput"] input {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 12px;
        color: white;
        padding: 14px;
        font-size: 15px;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #ff4d78;
        box-shadow: 0 0 0 1px #ff4d78;
    }

    /* ---------- Button ---------- */

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 13px 20px;
        border: none;
        font-weight: 700;
        font-size: 15px;
        background: linear-gradient(
            90deg,
            #ff174f,
            #ff4d78
        );
        color: white;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 23, 79, 0.30);
    }

    /* ---------- Report ---------- */

    .report-header {
        margin-top: 35px;
        padding: 20px 24px;
        border-radius: 16px 16px 0 0;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
    }

    .report-title {
        font-size: 24px;
        font-weight: 700;
    }

    .report-subtitle {
        color: #8f98a8;
        font-size: 13px;
    }

    .report-body {
        padding: 25px;
        border-radius: 0 0 16px 16px;
        background: rgba(255,255,255,0.025);
        border: 1px solid rgba(255,255,255,0.08);
        border-top: none;
        line-height: 1.7;
    }

    /* ---------- Info Cards ---------- */

    .info-card {
        padding: 20px;
        border-radius: 16px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        height: 100%;
    }

    .info-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }

    .info-title {
        font-weight: 700;
        font-size: 16px;
        margin-bottom: 5px;
    }

    .info-text {
        color: #929aaa;
        font-size: 13px;
        line-height: 1.5;
    }

    /* ---------- Footer ---------- */

    .footer {
        text-align: center;
        margin-top: 60px;
        padding: 25px;
        color: #687080;
        font-size: 13px;
        border-top: 1px solid rgba(255,255,255,0.06);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD AGENT
# ============================================================

@st.cache_resource
def get_agent():
    return youtube_agent()


try:
    agent = get_agent()

    if agent is None:
        st.error("❌ Agent initialization failed.")
        st.stop()

except Exception as e:
    st.error("❌ Unable to initialize the YouTube AI agent.")
    st.exception(e)
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🎥 YouTube AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">'
        'Transform long YouTube videos into structured, '
        'easy-to-understand insights.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✨ What it can do")

    st.markdown(
        """
        <div class="feature-card">
            🎯 <b>Video Overview</b><br>
            <span class="sidebar-text">
            Understand the video's type, structure and purpose.
            </span>
        </div>

        <div class="feature-card">
            ⏱️ <b>Smart Timestamps</b><br>
            <span class="sidebar-text">
            Identify important sections and topic transitions.
            </span>
        </div>

        <div class="feature-card">
            🧠 <b>AI Analysis</b><br>
            <span class="sidebar-text">
            Extract important concepts and learning points.
            </span>
        </div>

        <div class="feature-card">
            📚 <b>Content Organization</b><br>
            <span class="sidebar-text">
            Group related topics into meaningful sections.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.caption("Powered by Agno + Groq + YouTube Tools")


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✨ AI-POWERED VIDEO INTELLIGENCE
        </div>

        <div class="hero-title">
            YouTube AI Analyzer
        </div>

        <div class="hero-subtitle">
            Turn lengthy YouTube videos into structured insights,
            meaningful timestamps, key concepts and easy-to-read
            summaries — powered by an intelligent AI agent.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ANALYZER SECTION
# ============================================================

st.markdown(
    """
    <div class="analyzer-card">

        <div class="section-title">
            🔍 Analyze a YouTube Video
        </div>

        <div class="section-subtitle">
            Paste a YouTube URL below and let the AI agent analyze it.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


video_url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=...",
    label_visibility="collapsed"
)


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    analyze_button = st.button(
        "🚀 Analyze Video"
    )


# ============================================================
# EXAMPLE
# ============================================================

if not video_url:

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#737b8c;
            margin-top:10px;
            font-size:13px;
        ">
            💡 Try a tutorial, lecture, technical video or educational
            content.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ANALYSIS
# ============================================================

if video_url and analyze_button:

    if (
        "youtube.com" not in video_url
        and "youtu.be" not in video_url
    ):
        st.warning(
            "⚠️ Please enter a valid YouTube URL."
        )
        st.stop()

    with st.spinner("🧠 AI agent is analyzing your video..."):

        try:

            response = agent.run(
                f"""
                Analyze this YouTube video:

                {video_url}

                Provide a comprehensive analysis following
                your configured instructions.
                """
            )

            # Store response so it survives Streamlit reruns.
            st.session_state["analysis"] = response.content
            st.session_state["analyzed_url"] = video_url

        except Exception as e:

            st.error(
                "❌ Something went wrong while analyzing the video."
            )

            with st.expander("Show technical details"):
                st.exception(e)


# ============================================================
# DISPLAY REPORT
# ============================================================

if "analysis" in st.session_state:

    st.markdown(
        """
        <div class="report-header">

            <div class="report-title">
                📊 Video Analysis Report
            </div>

            <div class="report-subtitle">
                AI-generated insights and structured video breakdown
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="report-body">',
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state["analysis"]
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("")

    if st.session_state.get("analyzed_url"):

        st.caption(
            f"🔗 Analyzed video: "
            f"{st.session_state['analyzed_url']}"
        )


# ============================================================
# FEATURES
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        margin:30px 0 20px 0;
    ">
        <h2>⚡ Built for Smarter Video Consumption</h2>
        <p style="color:#8f98a8;">
            Save time. Understand more. Learn faster.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="info-card">

            <div class="info-icon">⏱️</div>

            <div class="info-title">
                Save Time
            </div>

            <div class="info-text">
                Quickly identify the most important parts
                of long-form YouTube content.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="info-card">

            <div class="info-icon">🧠</div>

            <div class="info-title">
                Learn Faster
            </div>

            <div class="info-text">
                Convert complex videos into structured,
                readable and useful information.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="info-card">

            <div class="info-icon">🎯</div>

            <div class="info-title">
                Find Key Moments
            </div>

            <div class="info-text">
                Discover important demonstrations,
                concepts and topic transitions.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        🎥 <b>YouTube AI Analyzer</b>
        <br><br>

        Built with Streamlit • Agno • Groq • YouTube Tools

    </div>
    """,
    unsafe_allow_html=True
)

