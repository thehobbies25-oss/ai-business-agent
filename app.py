import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Dua Shaikh — AI Business Agent",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# PREMIUM CSS
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    :root {
        --bg-primary: #050510;
        --bg-card: #0a0a1f;
        --bg-card-hover: #0f0f2a;
        --border: rgba(120,119,198,0.12);
        --border-hover: rgba(120,119,198,0.35);
        --accent: #7c6aef;
        --accent-light: #a594fd;
        --accent-glow: rgba(124,106,239,0.15);
        --text-primary: #f1f0ff;
        --text-secondary: #b4b0d4;
        --text-muted: #7b78a0;
        --success: #34d399;
        --warning: #fbbf24;
    }
    
    * { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    
    .stApp { background: var(--bg-primary); }
    
    #MainMenu, footer, header { visibility: hidden; }
    
    /* ======== HERO ======== */
    .hero {
        position: relative;
        background: linear-gradient(160deg, #0a0a20 0%, #12103a 45%, #0c0a22 100%);
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 55px 40px 50px;
        text-align: center;
        margin-bottom: 36px;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        inset: 0;
        background: 
            radial-gradient(ellipse at 20% 50%, rgba(124,106,239,0.06) 0%, transparent 60%),
            radial-gradient(ellipse at 80% 50%, rgba(167,139,250,0.05) 0%, transparent 60%);
        pointer-events: none;
    }
    
    .hero::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--accent), var(--accent-light), var(--accent), transparent);
    }
    
    .hero-logo {
        font-size: 3rem;
        margin-bottom: 12px;
        position: relative;
    }
    
    .hero h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 3.4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #c4b5fd 0%, #a78bfa 25%, #818cf8 50%, #a78bfa 75%, #c4b5fd 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite;
        margin: 0;
        line-height: 1.15;
        position: relative;
    }
    
    @keyframes textShine {
        to { background-position: 200% center; }
    }
    
    .hero-sub {
        color: #c8c3e3;
        font-size: 1.2rem;
        font-weight: 500;
        margin-top: 8px;
        position: relative;
    }
    
    .hero-desc {
        color: var(--text-secondary);
        font-size: 1.08rem;
        line-height: 1.8;
        max-width: 680px;
        margin: 18px auto 0;
        position: relative;
    }
    
    .hero-chip {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(124,106,239,0.12);
        border: 1px solid rgba(124,106,239,0.25);
        color: var(--accent-light);
        padding: 8px 22px;
        border-radius: 50px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 22px;
        position: relative;
    }
    
    /* ======== METRIC CARDS ======== */
    .metrics {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 18px;
        margin-bottom: 36px;
    }
    
    .mc {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 28px 22px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .mc::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--accent), transparent);
        opacity: 0;
        transition: opacity 0.4s;
    }
    
    .mc:hover {
        transform: translateY(-6px);
        border-color: var(--border-hover);
        box-shadow: 0 15px 40px var(--accent-glow);
    }
    
    .mc:hover::before { opacity: 1; }
    
    .mc-icon { font-size: 2.2rem; margin-bottom: 12px; }
    
    .mc-val {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 2.4rem;
        font-weight: 700;
        color: var(--text-primary);
    }
    
    .mc-label {
        color: var(--text-muted);
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        margin-top: 6px;
    }
    
    /* ======== TABS ======== */
    .stTabs [data-baseweb="tab-list"] {
        background: var(--bg-card);
        border-radius: 16px;
        padding: 6px;
        gap: 6px;
        border: 1px solid var(--border);
    }
    
    .stTabs [data-baseweb="tab"] {
        color: var(--text-muted);
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.02rem;
        padding: 14px 24px;
        transition: all 0.3s;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-secondary);
        background: rgba(124,106,239,0.06);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #5b47e0, #7c3aed) !important;
        color: #fff !important;
        box-shadow: 0 4px 15px rgba(124,106,239,0.3);
    }
    
    /* ======== SECTION TITLE ======== */
    .stitle {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 30px 0 18px;
        padding-bottom: 14px;
        border-bottom: 2px solid var(--border);
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    /* ======== FEATURE CARDS ======== */
    .fc {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 32px 24px;
        transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
        height: 100%;
    }
    
    .fc:hover {
        border-color: var(--border-hover);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px var(--accent-glow);
    }
    
    .fc-icon { font-size: 2.8rem; margin-bottom: 16px; }
    
    .fc-title {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 10px;
    }
    
    .fc-desc {
        color: var(--text-secondary);
        font-size: 1rem;
        line-height: 1.75;
    }
    
    /* ======== CHAT ======== */
    .chat-u {
        background: linear-gradient(145deg, #16143d, #1f1c52);
        border: 1px solid rgba(124,106,239,0.15);
        border-radius: 8px 20px 20px 20px;
        padding: 22px 26px;
        margin: 16px 0;
        animation: msgIn 0.4s ease;
    }
    
    .chat-a {
        background: linear-gradient(145deg, #0b0f20, #101830);
        border: 1px solid rgba(99,102,241,0.1);
        border-left: 4px solid var(--accent);
        border-radius: 4px 20px 20px 20px;
        padding: 26px 28px;
        margin: 16px 0;
        animation: msgIn 0.4s ease;
    }
    
    @keyframes msgIn {
        from { opacity: 0; transform: translateY(16px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .chat-tag {
        font-size: 0.72rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 10px;
        color: var(--accent-light);
    }
    
    .chat-u .chat-text, .chat-a .chat-text {
        color: var(--text-primary);
        font-size: 1.06rem;
        line-height: 1.8;
    }
    
    /* ======== INPUTS ======== */
    .stTextInput input, .stTextArea textarea {
        background: #0c0c22 !important;
        border: 1px solid var(--border) !important;
        border-radius: 14px !important;
        color: var(--text-primary) !important;
        font-size: 1.02rem !important;
        padding: 14px 18px !important;
        transition: border-color 0.3s !important;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px var(--accent-glow) !important;
    }
    
    .stTextInput label, .stTextArea label, .stSelectbox label {
        color: #c8c3e3 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    .stSelectbox > div > div {
        background: #0c0c22 !important;
        border: 1px solid var(--border) !important;
        border-radius: 14px !important;
        color: var(--text-primary) !important;
    }
    
    /* ======== BUTTONS ======== */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #5b47e0, #7c3aed) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 14px 36px !important;
        font-weight: 800 !important;
        font-size: 1.02rem !important;
        letter-spacing: 0.3px !important;
        transition: all 0.35s !important;
        box-shadow: 0 4px 15px rgba(91,71,224,0.25) !important;
    }
    
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(91,71,224,0.4) !important;
    }
    
    .stButton > button {
        background: rgba(124,106,239,0.08) !important;
        color: var(--accent-light) !important;
        border: 1px solid rgba(124,106,239,0.2) !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        padding: 12px 20px !important;
        transition: all 0.35s !important;
    }
    
    .stButton > button:hover {
        background: rgba(124,106,239,0.15) !important;
        border-color: rgba(124,106,239,0.4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px var(--accent-glow) !important;
    }
    
    .stDownloadButton > button {
        background: linear-gradient(135deg, #047857, #059669) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 800 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(4,120,87,0.25) !important;
    }
    
    /* Chat Input */
    .stChatInput > div {
        background: #0c0c22 !important;
        border: 1px solid var(--border) !important;
        border-radius: 16px !important;
    }
    .stChatInput input {
        color: var(--text-primary) !important;
        font-size: 1.06rem !important;
    }
    
    /* Metrics */
    [data-testid="stMetric"] {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 20px;
    }
    [data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-size: 1.9rem !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-size: 0.9rem !important;
    }
    
    /* Markdown */
    .stMarkdown p, .stMarkdown li {
        color: #c8c3e3;
        font-size: 1.04rem;
        line-height: 1.85;
    }
    .stMarkdown h1 { color: #f1f0ff; font-size: 2.1rem; font-family: 'Space Grotesk', sans-serif !important; }
    .stMarkdown h2 { color: #d4d0f0; font-size: 1.65rem; font-family: 'Space Grotesk', sans-serif !important; }
    .stMarkdown h3 { color: #c4b5fd; font-size: 1.35rem; font-family: 'Space Grotesk', sans-serif !important; }
    .stMarkdown h4 { color: #a78bfa; font-size: 1.15rem; }
    .stMarkdown strong { color: #f1f0ff; }
    .stMarkdown em { color: #a09cc0; }
    
    /* Tables */
    .stMarkdown table { width: 100%; border-collapse: collapse; margin: 16px 0; }
    .stMarkdown th {
        background: rgba(124,106,239,0.12);
        color: #d4d0f0;
        padding: 14px 18px;
        text-align: left;
        font-weight: 700;
        font-size: 0.95rem;
        border-bottom: 2px solid rgba(124,106,239,0.15);
    }
    .stMarkdown td {
        padding: 12px 18px;
        border-bottom: 1px solid rgba(124,106,239,0.06);
        color: #c8c3e3;
        font-size: 0.97rem;
    }
    .stMarkdown tr:hover td { background: rgba(124,106,239,0.04); }
    
    .stMarkdown code {
        background: rgba(124,106,239,0.1);
        color: var(--accent-light);
        padding: 3px 8px;
        border-radius: 6px;
    }
    
    hr { border-color: var(--border) !important; }
    .stCaption { color: var(--text-muted) !important; }
    .stAlert { border-radius: 14px !important; }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #06060f;
        border-right: 1px solid var(--border);
    }
    
    /* Badge */
    .b-on {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(52,211,153,0.1);
        color: #34d399;
        border: 1px solid rgba(52,211,153,0.2);
        padding: 6px 16px;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 700;
    }
    .b-demo {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(251,191,36,0.08);
        color: #fbbf24;
        border: 1px solid rgba(251,191,36,0.15);
        padding: 6px 16px;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 700;
    }
    
    /* Footer */
    .ft {
        text-align: center;
        padding: 40px 20px;
        margin-top: 60px;
        border-top: 1px solid var(--border);
    }
    .ft-name {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--accent-light);
    }
    .ft p { color: var(--text-muted); font-size: 0.92rem; margin: 4px 0; }
    .ft a { color: var(--accent-light); text-decoration: none; font-weight: 700; }
    .ft a:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

# ============================================
# STATE
# ============================================
if "chats" not in st.session_state:
    st.session_state.chats = []
if "data" not in st.session_state:
    st.session_state.data = None
if "done" not in st.session_state:
    st.session_state.done = 0

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("# ⚡ AI Agent")
    st.caption("by Dua Shaikh")
    st.divider()
    
    st.markdown("### 🔑 API Connection")
    api_key = st.text_input("OpenAI API Key:", type="password", placeholder="sk-...")
    
    client = None
    if api_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            st.markdown('<span class="b-on">⚡ Connected</span>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ {e}")
    else:
        st.markdown('<span class="b-demo">◐ Demo Mode</span>', unsafe_allow_html=True)
        st.caption("Add API key for full AI capabilities")
    
    st.divider()
    st.markdown("### 🧠 Configuration")
    model = st.selectbox("Model:", ["gpt-4o-mini","gpt-4o","gpt-3.5-turbo"])
    temp = st.slider("Creativity:", 0.0, 1.0, 0.1, 0.05)
    
    st.divider()
    st.markdown("### 📁 Data")
    csv_file = st.file_uploader("Upload CSV", type=["csv"])
    if csv_file:
        st.session_state.data = pd.read_csv(csv_file)
        st.success(f"✅ {len(st.session_state.data)} rows loaded")
    
    st.divider()
    st.markdown("**Dua Shaikh**")
    st.caption("AI Engineer & Automation Specialist")
    st.caption("[LinkedIn](https://linkedin.com) · [GitHub](https://github.com)")

# ============================================
# HERO
# ============================================
st.markdown("""
<div class="hero">
    <div class="hero-logo">⚡</div>
    <h1>AI Business Agent</h1>
    <div class="hero-sub">Intelligent Automation for Modern Businesses</div>
    <div class="hero-desc">
        A comprehensive AI-powered platform that handles data analysis, 
        professional email drafting, strategic report generation, and 
        real-time business intelligence — designed to save you hours 
        of work every single day.
    </div>
    <div class="hero-chip">✦ Developed by Dua Shaikh</div>
</div>
""", unsafe_allow_html=True)

# ============================================
# METRICS
# ============================================
n_chats = len([m for m in st.session_state.chats if m["role"]=="user"])
n_rows = len(st.session_state.data) if st.session_state.data is not None else 0
s_txt = "Online" if client else "Demo"
s_clr = "#34d399" if client else "#fbbf24"

st.markdown(f"""
<div class="metrics">
    <div class="mc">
        <div class="mc-icon">💬</div>
        <div class="mc-val">{n_chats}</div>
        <div class="mc-label">Conversations</div>
    </div>
    <div class="mc">
        <div class="mc-icon">⚡</div>
        <div class="mc-val" style="color:{s_clr};font-size:1.6rem">{s_txt}</div>
        <div class="mc-label">System Status</div>
    </div>
    <div class="mc">
        <div class="mc-icon">📊</div>
        <div class="mc-val">{n_rows}</div>
        <div class="mc-label">Data Points</div>
    </div>
    <div class="mc">
        <div class="mc-icon">✅</div>
        <div class="mc-val">{st.session_state.done}</div>
        <div class="mc-label">Tasks Done</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# TABS
# ============================================
tab1, tab2, tab3, tab4 = st.tabs([
    "🤖 AI Assistant", "📊 Data Analyst",
    "✉️ Email Studio", "📋 Report Builder"
])

# ============================================
# TAB 1: AI ASSISTANT
# ============================================
with tab1:
    st.markdown('<div class="stitle">🤖 AI Business Assistant</div>', unsafe_allow_html=True)
    
    if len(st.session_state.chats) == 0:
        a, b, c, d = st.columns(4)
        with a:
            st.markdown("""<div class="fc">
                <div class="fc-icon">📊</div>
                <div class="fc-title">Market Intelligence</div>
                <div class="fc-desc">Deep market research with real data, competitor mapping, growth trends and strategic opportunities</div>
            </div>""", unsafe_allow_html=True)
        with b:
            st.markdown("""<div class="fc">
                <div class="fc-icon">✉️</div>
                <div class="fc-title">Email Copywriting</div>
                <div class="fc-desc">Craft professional, high-converting emails that build relationships and close deals faster</div>
            </div>""", unsafe_allow_html=True)
        with c:
            st.markdown("""<div class="fc">
                <div class="fc-icon">🎯</div>
                <div class="fc-title">Business Strategy</div>
                <div class="fc-desc">SWOT analysis, competitive strategy, growth planning and actionable business roadmaps</div>
            </div>""", unsafe_allow_html=True)
        with d:
            st.markdown("""<div class="fc">
                <div class="fc-icon">📋</div>
                <div class="fc-title">Auto Reports</div>
                <div class="fc-desc">Generate executive-grade reports with KPIs, trends, risk analysis and clear recommendations</div>
            </div>""", unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("**⚡ Quick Actions**")
    q1, q2, q3, q4 = st.columns(4)
    quick = None
    with q1:
        if st.button("📊 Market Analysis", use_container_width=True):
            quick = "I need a comprehensive market analysis of the AI industry for 2026-2027. Cover market size, growth rate, top players, emerging trends, biggest opportunities, key challenges, and strategic recommendations for someone building an AI business."
    with q2:
        if st.button("✉️ Draft Email", use_container_width=True):
            quick = "Write a professional business email to a client informing them about a completed AI automation project. Include project highlights, key results with specific numbers, ROI metrics, and a suggestion for Phase 2."
    with q3:
        if st.button("📋 Business Plan", use_container_width=True):
            quick = "Create a comprehensive business plan for an AI consulting startup. Include executive summary, market opportunity, services with pricing, revenue projections for 3 years, competitive advantages, and go-to-market strategy."
    with q4:
        if st.button("🎯 SWOT Analysis", use_container_width=True):
            quick = "Conduct a thorough SWOT analysis for a technology startup entering the AI/ML market in 2026. Provide at least 5 detailed points in each category with specific examples and actionable recommendations."
    
    st.divider()
    
    for msg in st.session_state.chats:
        if msg["role"] == "user":
            st.markdown(f"""<div class="chat-u">
                <div class="chat-tag">👤 You</div>
                <div class="chat-text">{msg["content"]}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="chat-a"><div class="chat-tag">🤖 AI Agent</div></div>""", unsafe_allow_html=True)
            st.markdown(msg["content"])
    
    user_input = st.chat_input("Ask me anything about business, strategy, or analysis...")
    prompt = quick or user_input
    
    if prompt:
        st.session_state.chats.append({"role":"user","content":prompt})
        
        if client:
            with st.spinner("Working on your request..."):
                try:
                    msgs = [{"role":"system","content":"""You are a senior business consultant embedded 
inside a custom AI platform built by Dua Shaikh. Provide world-class business advice.

Rules:
- Be extremely detailed with specific numbers, percentages, data
- Use clear headers (##), bullet points, and markdown tables
- Write in a natural, confident, human tone
- Include actionable recommendations with priorities
- End with clear next steps
- Never mention ChatGPT, OpenAI, or that you're an AI language model
- You are the intelligence engine of this platform"""}]
                    
                    for m in st.session_state.chats[-10:]:
                        msgs.append({"role":m["role"],"content":m["content"]})
                    
                    r = client.chat.completions.create(model=model, messages=msgs, temperature=temp, max_tokens=3500)
                    reply = r.choices[0].message.content
                    st.session_state.chats.append({"role":"assistant","content":reply})
                    st.session_state.done += 1
                    st.rerun()
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
        else:
            p = prompt.lower()
            if any(w in p for w in ["market","analysis","trend","industry"]):
                reply = """## 📊 AI Market Analysis — 2026-2027

### Executive Overview

The global AI market has crossed **$640 billion in 2026** and is projected to reach **$830 billion by the end of 2027** — a compound annual growth rate of roughly 28%. This makes AI the fastest-growing sector in the technology industry by a significant margin.

### Market Breakdown

| Segment | 2026 Value | 2027 Projected | YoY Growth |
|---------|-----------|----------------|-----------|
| Enterprise AI | $398B | $513B | +28.9% |
| Generative AI Applications | $89B | $142B | +59.6% |
| AI Agents & Autonomous Systems | $12B | $28B | +133% |
| AI Security & Safety | $24B | $41B | +70.8% |
| AI Infrastructure / MLOps | $45B | $67B | +48.9% |
| Edge AI / On-Device | $18B | $29B | +61.1% |

### Fastest Growing Segments

The numbers tell a clear story about where the market is heading:

**1. AI Agents & Autonomous Systems (+133%)** — This is the breakout category. Companies don't just want chatbots anymore. They want AI that can actually execute tasks independently — process invoices, handle customer support end-to-end, manage scheduling, and make decisions. If you're building AI agents, you're in the right place at the right time.

**2. AI Security (+71%)** — As AI becomes critical business infrastructure, protecting it becomes essential. Prompt injection attacks, model poisoning, data extraction — these are real threats now. Companies are paying premium prices for AI security expertise.

**3. Generative AI Applications (+60%)** — Content creation, code generation, design automation. Every department in every company is finding ways to use generative AI to move faster.

**4. Edge AI (+61%)** — Running AI models directly on devices instead of the cloud. Privacy-sensitive industries like healthcare and finance are driving this hard.

### Competitive Landscape

| Company | Estimated Revenue | Key Strength | Market Position |
|---------|------------------|-------------|-----------------|
| OpenAI | ~$29B | GPT ecosystem, brand dominance | Market leader |
| Google DeepMind | ~$22B | Gemini + Cloud integration | Strong #2 |
| Anthropic | ~$8B | Claude, enterprise safety focus | Fastest growing |
| Meta AI | Open source | Llama ecosystem, community | Open source leader |
| Microsoft | ~$18B | Copilot suite, enterprise integration | Enterprise leader |

### The Untapped Opportunity

Here's what most people miss: **76% of mid-market companies** (50-500 employees) want AI capabilities but don't have the technical team to build them. They have budget. They have problems. They need someone who can deliver solutions and explain them in plain business language.

This is a massive, underserved market. The big consulting firms charge too much. The freelancers lack credibility. There's a sweet spot for specialized AI consultants who can deliver fast, communicate clearly, and charge fairly.

### Strategic Recommendations

1. **Focus on AI Agents** — Highest growth (133%), clients pay $5K-$80K per project, and competition is still relatively low because the technology is new
2. **Target mid-market businesses** — They have real budgets ($10K-$100K), faster decision cycles than enterprise, and genuine need for AI expertise
3. **Build working demos** — Nothing sells like a live product someone can click on and test
4. **Price on value, not time** — If your AI saves a company $200K per year, charging $30K for it is easy to justify
5. **Create recurring revenue** — Monthly support contracts ($2K-$10K/month) build predictable income

### What's Coming Next

By late 2027, expect to see:
- AI Agents handling 35-40% of routine business operations
- Voice AI becoming the default for customer service interactions
- Mandatory AI governance and compliance requirements in EU and US
- Every SaaS product either adding AI features or losing market share
- Explosive demand for AI safety, compliance, and red-teaming expertise

---
*Detailed market intelligence powered by the AI Business Agent platform.*"""

            elif any(w in p for w in ["email","write","draft","mail"]):
                today = datetime.now().strftime("%B %d, %Y")
                reply = f"""## ✉️ Professional Email Draft

---

**Subject:** Project Complete — Here's What We Achieved Together

**Date:** {today}

---

Hi there,

Wanted to share some great news — we've successfully deployed the AI automation system, and the early results are already better than we projected.

### Here's What We Delivered

| Module | Status | Business Impact |
|--------|--------|----------------|
| Document Processing AI | ✅ Live | 87% faster processing |
| Smart Email Automation | ✅ Live | 14 hours saved per week |
| Analytics Dashboard | ✅ Live | Real-time insights across all departments |
| Customer Support Bot | ✅ Live | Handling 73% of inquiries autonomously |

### The Numbers

Let me put the results in perspective:

- **Processing speed improved 87%** — what took 45 minutes now takes under 6
- **Projected annual savings: $340,000** in operational costs
- **14 hours freed up every week** for your team — that's nearly 2 full work days
- **Customer response time dropped from 4 hours to 11 minutes**
- **System accuracy: 94.7%** and improving with every interaction

### Return on Investment

- **Total investment:** $125,000
- **Annual savings:** $340,000
- **First-year ROI:** 172%
- **Payback period:** 4.4 months

You'll recover the entire investment before summer.

### What I'd Recommend Next

Based on what I've observed in your operations, two areas could deliver significant additional value:

**1. Sales Intelligence Module** — AI analysis of your CRM data to predict which leads are most likely to convert and automatically prioritize your pipeline. Based on similar implementations, this could improve close rates by 20-30%.

**2. Automated Financial Reporting** — Replace the 3-day monthly reporting cycle with an AI system that generates comprehensive reports in minutes, complete with trend analysis and anomaly detection.

Would you have 30 minutes this week for a quick call to walk through the detailed results? I can share the full dashboard and discuss the Phase 2 roadmap.

Looking forward to connecting.

Best regards,

**Dua Shaikh**
AI Solutions & Automation
📧 duashaikh@email.com

---
*Email drafted using the AI Business Agent platform.*"""

            elif any(w in p for w in ["plan","business","startup"]):
                reply = """## 📋 Business Plan — AI Consulting Startup

---

### Executive Summary

**Company:** IntelliForce AI Solutions
**Founder:** Dua Shaikh
**Mission:** Help mid-market businesses unlock AI without needing a technical team
**Funding Target:** $500K seed round
**Revenue Projection:** $1.2M (Year 1) → $3.4M (Year 2) → $5.8M (Year 3)

The AI consulting market is projected to hit $64 billion by 2027. Yet 76% of mid-market companies still don't have AI capabilities — not because they don't want them, but because they lack the expertise to implement them. That gap is our opportunity.

---

### The Problem

Most businesses understand they need AI. But they face three barriers:

1. **No AI engineers on staff** — Hiring takes 6+ months and costs $150K+ per person
2. **Overwhelmed by options** — The AI landscape changes every month. What works? What's hype?
3. **Bad past experiences** — Many have paid consultants who over-promised and under-delivered

We solve all three. We come in, identify the highest-impact use cases, build the solution, and provide ongoing support.

---

### Services & Pricing

| Service | Deliverable | Price Range | Profit Margin |
|---------|------------|-------------|---------------|
| AI Strategy Workshop | Roadmap + prioritized use cases | $3K - $8K | 85% |
| Custom AI Agent Development | Autonomous AI for specific tasks | $10K - $80K | 65% |
| Document AI / RAG Systems | Chat with company data & documents | $8K - $40K | 70% |
| Process Automation | End-to-end workflow automation | $5K - $35K | 72% |
| Monthly AI Support | Maintenance + optimization + updates | $2K - $10K/mo | 82% |
| Team Training Programs | Upskill client teams on AI tools | $3K - $15K | 88% |

---

### Financial Projections

| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Revenue | $1.2M | $3.4M | $5.8M |
| Gross Profit | $840K | $2.4M | $4.1M |
| Net Profit | $180K | $680K | $1.5M |
| Profit Margin | 15% | 20% | 26% |
| Clients | 24 | 68 | 115 |
| Team Size | 4 | 11 | 20 |
| Avg Deal Size | $22K | $28K | $35K |

### Year 1 Revenue Mix

| Source | Revenue | Share |
|--------|---------|-------|
| Custom AI Development | $480K | 40% |
| Monthly Support Contracts | $240K | 20% |
| Strategy Consulting | $216K | 18% |
| Training & Workshops | $144K | 12% |
| Process Automation | $120K | 10% |

---

### Competitive Advantages

1. **3x Faster Delivery** — We use AI to build AI. What takes traditional agencies 3 months, we deliver in 3-4 weeks
2. **40% Lower Cost** — Lean team, no massive overhead. We pass those savings to clients
3. **We Speak Business** — No confusing jargon. Every conversation is about ROI, time saved, and revenue impact
4. **Results-Based Options** — We offer performance-based pricing because we trust our own work
5. **Ongoing Partnership** — We don't disappear after deployment. Monthly support keeps everything optimized

---

### Go-to-Market Strategy

**Month 1-3:** Build 5 portfolio projects with live demos. Land 3 pilot clients at 50% discount in exchange for testimonials and case studies.

**Month 4-6:** Launch content marketing engine — weekly LinkedIn posts, case study breakdowns, AI insights. Start cold outreach to mid-market companies. Activate referral program.

**Month 7-12:** Hire 2 additional engineers. Launch productized AI packages (fixed-price, fixed-scope). Build partnerships with 2-3 digital agencies. Attend industry conferences.

---

### Funding Allocation

| Category | Amount | Purpose |
|----------|--------|---------|
| Engineering Team | $250K | 3 senior AI engineers |
| Marketing & Sales | $100K | Content, ads, CRM, tools |
| Cloud Infrastructure | $75K | Compute, APIs, hosting |
| Operating Capital | $75K | 6-month runway |

---

### The Bottom Line

With $500K in seed capital, we project profitability by Month 8 and a path to $5.8M revenue by Year 3. The AI consulting market is growing 35% annually, and the mid-market segment is massively underserved.

This is the right market, the right timing, and the right team.

---
*Business plan generated by the AI Business Agent platform developed by Dua Shaikh.*"""

            elif any(w in p for w in ["swot","strength","weakness"]):
                reply = """## 🎯 SWOT Analysis — AI Startup 2026

---

### 💪 Strengths

| # | Strength | Strategic Value |
|---|----------|----------------|
| 1 | **Deep AI/ML expertise across LLMs, RAG, and AI Agents** | Can deliver solutions that most agencies only talk about |
| 2 | **Extremely low operating costs** — remote team, cloud-native | High margins even at competitive pricing |
| 3 | **AI-accelerated development process** | 3x faster delivery than traditional development shops |
| 4 | **Specialized focus on AI Agents** — the fastest-growing segment | Positioned in a 133% CAGR market before it gets crowded |
| 5 | **Working portfolio with live, clickable demos** | Massive trust advantage — clients can test before buying |
| 6 | **Technical founder who speaks business** | Can sell to executives AND build the product — rare combination |

**Key Takeaway:** We're specialized, fast, lean, and positioned in the hottest segment of AI.

---

### 🔴 Weaknesses

| # | Weakness | Mitigation Plan |
|---|----------|----------------|
| 1 | **No brand recognition yet** | Aggressive LinkedIn content + case studies from first 5 clients |
| 2 | **Small team limits project capacity** | Strategic hiring as revenue grows + contractor network for overflow |
| 3 | **No enterprise client references** | Start with SMBs, build credibility, then move upmarket over 12 months |
| 4 | **Dependent on third-party AI APIs** (OpenAI, etc.) | Develop expertise with open-source models (Llama, Mistral) as fallback |
| 5 | **No dedicated sales team** | Founder-led sales initially, hire dedicated sales by Month 6 |

**Key Takeaway:** These are standard early-stage challenges. Every one has a clear, executable solution with a timeline.

---

### 🟢 Opportunities

| # | Opportunity | Market Size | Our Approach |
|---|------------|-------------|-------------|
| 1 | **76% of mid-market companies need AI but can't build it** | $50B+ market | Be their outsourced AI team |
| 2 | **AI Agent market growing 133% annually** | $28B by 2027 | Lead with agent development services |
| 3 | **Government AI adoption mandates increasing** | $15B+ | Pursue public sector contracts |
| 4 | **Every SaaS company racing to add AI features** | Massive | Offer AI integration as a service |
| 5 | **Corporate AI training demand exploding** | $12B | High-margin training and workshops |
| 6 | **Healthcare AI adoption just beginning** | $45B by 2027 | Develop health-tech specialization |

**Key Takeaway:** The market is enormous, growing fast, and still underserved. We just need to pick our lane and execute consistently.

---

### ⚠️ Threats

| # | Threat | Probability | Impact | Our Response |
|---|--------|-------------|--------|-------------|
| 1 | **Big tech offering cheap, commoditized AI tools** | High | Medium | We customize and integrate — generic tools can't replace that |
| 2 | **Rapidly changing AI regulations** (EU AI Act, etc.) | Medium | Medium | Build compliance into every project from day one |
| 3 | **Technology evolving every 3-6 months** | High | Low | Continuous learning is built into our culture — it's an advantage |
| 4 | **Price competition from offshore development teams** | Medium | Medium | Compete on quality, speed, and communication — not price |
| 5 | **Client data security concerns slowing adoption** | Medium | Medium | Implement SOC2-level security practices from the start |
| 6 | **Economic recession reducing technology budgets** | Low | High | Position AI as a cost-cutting investment, not a luxury expense |

**Key Takeaway:** Every threat has a counter-strategy. The key advantage of being small is agility — we can adapt faster than any large competitor.

---

### 📌 Action Plan

**This Month**
1. Complete 5 portfolio projects with live demos
2. Lock in 3 pilot clients for testimonials
3. Start weekly LinkedIn content publishing

**Next 90 Days**
4. Close first $50K in revenue
5. Hire first AI engineer
6. Launch presence on Upwork and Fiverr for additional deal flow

**6 Months**
7. Reach $200K cumulative revenue
8. Build partnerships with 2 established digital agencies
9. Launch monthly AI insights newsletter for thought leadership

**12 Months**
10. Hit $1M+ annual run rate
11. Team of 5-6 specialists
12. Begin enterprise outreach backed by case studies and proven results

---
*Strategic analysis generated by Dua Shaikh's AI Business Agent platform.*"""
            else:
                reply = f"""## Welcome to the AI Business Agent

Thanks for reaching out! Here's a quick overview of everything this platform can do for you:

### What You Asked

*"{prompt[:250]}"*

### Available Capabilities

| Module | What It Does | Best For |
|--------|-------------|----------|
| **🤖 AI Assistant** | Strategic advice, market research, competitive analysis | Quick answers and deep business insights |
| **📊 Data Analyst** | Upload CSV data, get charts, statistics, and AI insights | Performance tracking, sales analysis |
| **✉️ Email Studio** | Professional email drafting for any situation | Client communication, outreach, proposals |
| **📋 Report Builder** | Auto-generate detailed business reports | Executive summaries, quarterly reviews |

### Try These Prompts

- *"Analyze the AI agent market — where's the biggest opportunity?"*
- *"Write a follow-up email to a client who hasn't responded in a week"*
- *"Create a quarterly performance report for my startup"*
- *"What's the best pricing strategy for AI consulting services?"*
- *"Compare the top 5 AI frameworks for enterprise applications"*

### Getting Full AI Power

Connect your OpenAI API key in the sidebar to unlock:
- ✅ Custom responses tailored to your exact questions
- ✅ Real-time analysis of your uploaded datasets
- ✅ Unlimited email drafting and report generation
- ✅ Deep strategic analysis for any industry or market

You can get an API key at **platform.openai.com** — takes about 2 minutes.

---
*Built by Dua Shaikh — AI Solutions & Automation*"""
            
            st.session_state.chats.append({"role":"assistant","content":reply})
            st.session_state.done += 1
            st.rerun()

# ============================================
# TAB 2: DATA ANALYST
# ============================================
with tab2:
    st.markdown('<div class="stitle">📊 Data Analyst</div>', unsafe_allow_html=True)
    
    if st.session_state.data is not None:
        df = st.session_state.data
        nc = df.select_dtypes(include='number').columns.tolist()
        cc = df.select_dtypes(include='object').columns.tolist()
        
        a,b,c,d = st.columns(4)
        with a: st.metric("📋 Rows", f"{len(df):,}")
        with b: st.metric("📊 Columns", len(df.columns))
        with c: st.metric("🔢 Numeric", len(nc))
        with d: st.metric("📝 Categorical", len(cc))
        
        st.divider()
        st.markdown("#### 📋 Data Preview")
        st.dataframe(df.head(10), use_container_width=True, height=320)
        
        st.markdown("#### 📈 Statistics")
        st.dataframe(df.describe().round(2), use_container_width=True)
        
        if nc:
            st.divider()
            st.markdown("#### 📊 Visualizations")
            
            v1, v2 = st.columns(2)
            with v1:
                hc = st.selectbox("Metric:", nc, key="hc")
                fig = px.histogram(df, x=hc, title=f"Distribution — {hc}", color_discrete_sequence=["#7c6aef"], template="plotly_dark")
                fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#c8c3e3',size=13), title_font=dict(color='#f1f0ff',size=17))
                st.plotly_chart(fig, use_container_width=True)
            
            with v2:
                if len(nc) >= 2:
                    xc2 = st.selectbox("X:", nc, key="xc2")
                    yc2 = st.selectbox("Y:", nc, index=min(1,len(nc)-1), key="yc2")
                    clr = None
                    if cc:
                        clr = st.selectbox("Color:", [None]+cc, key="clr")
                    fig2 = px.scatter(df, x=xc2, y=yc2, color=clr, title=f"{xc2} vs {yc2}", template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Set2)
                    fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#c8c3e3',size=13), title_font=dict(color='#f1f0ff',size=17))
                    st.plotly_chart(fig2, use_container_width=True)
            
            if cc and nc:
                st.markdown("#### 📊 Category Breakdown")
                g1,g2,g3 = st.columns(3)
                with g1: gb = st.selectbox("Group:", cc, key="gb")
                with g2: ms = st.selectbox("Measure:", nc, key="ms")
                with g3: ag = st.selectbox("Calc:", ["sum","mean","count","max","min"], key="ag")
                
                gd = df.groupby(gb)[ms].agg(ag).reset_index().sort_values(ms, ascending=False)
                fig3 = px.bar(gd, x=gb, y=ms, title=f"{ag.title()} of {ms} by {gb}", color=ms, color_continuous_scale="Viridis", template="plotly_dark")
                fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#c8c3e3',size=13), title_font=dict(color='#f1f0ff',size=17))
                st.plotly_chart(fig3, use_container_width=True)
                
                st.markdown("#### 🥧 Proportions")
                p1,p2 = st.columns(2)
                with p1: pc = st.selectbox("Category:", cc, key="pc")
                with p2: pv = st.selectbox("Values:", nc, key="pv")
                pd2 = df.groupby(pc)[pv].sum().reset_index()
                fig4 = px.pie(pd2, names=pc, values=pv, title=f"{pv} by {pc}", template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Set2)
                fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#c8c3e3',size=13), title_font=dict(color='#f1f0ff',size=17))
                st.plotly_chart(fig4, use_container_width=True)
        
        st.divider()
        st.markdown("#### 🤖 Ask About Your Data")
        dq = st.text_input("Your question:", placeholder="e.g., Which product has the highest revenue?")
        
        if dq:
            if client:
                with st.spinner("Analyzing..."):
                    try:
                        dp = f"""You are a senior data analyst inside a platform built by Dua Shaikh.
Analyze this dataset:
Columns: {list(df.columns)}
Types: {df.dtypes.to_dict()}
Shape: {df.shape}
Stats: {df.describe().to_string()}
Data: {df.to_string()}

Question: {dq}

Give detailed answer with specific numbers, tables, rankings, patterns, and recommendations.
Write naturally and confidently."""
                        r = client.chat.completions.create(model=model, messages=[{"role":"user","content":dp}], temperature=0.1, max_tokens=2000)
                        st.markdown(r.choices[0].message.content)
                        st.session_state.done += 1
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.markdown(f"""### Quick Analysis

**Question:** *{dq}*

| Column | Average | Maximum | Minimum | Total |
|--------|---------|---------|---------|-------|""")
                for col in nc[:5]:
                    st.markdown(f"| {col} | {df[col].mean():,.2f} | {df[col].max():,.2f} | {df[col].min():,.2f} | {df[col].sum():,.2f} |")
                st.info("🔑 Connect your API key for deep AI-powered analysis with custom insights.")
                st.session_state.done += 1
    else:
        st.markdown("""<div class="fc" style="text-align:center;padding:60px;">
            <div class="fc-icon">📊</div>
            <div class="fc-title" style="font-size:1.5rem;">Upload Your Data</div>
            <div class="fc-desc" style="font-size:1.1rem;">
                Upload any CSV file using the sidebar to get instant charts, 
                statistics, and AI-powered insights. You can ask questions 
                about your data in plain English.
            </div>
        </div>""", unsafe_allow_html=True)
        
        st.markdown("")
        if st.button("📊 Try With Sample Data", type="primary", use_container_width=True):
            st.session_state.data = pd.DataFrame({
                'Product': ['AI Chatbot','AI Agent','RAG System','Voice AI','AI Chatbot','AI Agent','RAG System','Voice AI','AI Chatbot','AI Agent'],
                'Quarter': ['Q1','Q1','Q1','Q1','Q2','Q2','Q2','Q2','Q3','Q3'],
                'Units Sold': [15,8,12,6,22,14,18,11,28,19],
                'Revenue': [75000,120000,96000,54000,110000,210000,144000,99000,140000,285000],
                'Profit': [45000,78000,62000,32000,72000,147000,100000,69000,98000,199000],
                'Customers': [12,5,8,4,18,9,14,7,22,12],
                'Region': ['North','South','East','West','North','South','East','West','North','South'],
                'Satisfaction': [4.5,4.8,4.3,4.1,4.6,4.9,4.4,4.2,4.7,4.9]
            })
            st.rerun()

# ============================================
# TAB 3: EMAIL STUDIO
# ============================================
with tab3:
    st.markdown('<div class="stitle">✉️ Email Studio</div>', unsafe_allow_html=True)
    
    e1,e2 = st.columns(2)
    with e1:
        et = st.selectbox("📨 Type:", ["Professional Update","Client Follow-up","Project Completion","Meeting Request","Business Proposal","Cold Outreach","Thank You","Partnership Inquiry","Job Application","Issue Resolution"])
        to = st.text_input("👤 To:", placeholder="e.g., Sarah Johnson, VP Engineering")
        sb = st.text_input("📌 Subject:", placeholder="e.g., AI Project Results — 87% Efficiency Gain")
        fr = st.text_input("✍️ From:", value="Dua Shaikh")
    with e2:
        tn = st.selectbox("🎭 Tone:", ["Professional & Confident","Friendly & Warm","Formal & Corporate","Persuasive & Compelling","Empathetic","Enthusiastic"])
        ln = st.selectbox("📏 Length:", ["Concise (3-5 sentences)","Standard (2 paragraphs)","Detailed (3-4 paragraphs)","Comprehensive"])
        ur = st.selectbox("⏰ Priority:", ["Normal","Urgent","Follow-up","FYI"])
        cx = st.text_area("📝 Key Points:", placeholder="What should the email cover? Specific details, numbers, requests...", height=132)
    
    if st.button("✍️ Generate Email", type="primary", use_container_width=True):
        if client:
            with st.spinner("Crafting your email..."):
                try:
                    ep = f"""Write a world-class {et} email.
To: {to} | From: {fr} | Subject: {sb}
Tone: {tn} | Length: {ln} | Priority: {ur}
Key Points: {cx}

Requirements:
- Compelling subject line
- Natural, human greeting (avoid clichés like "I hope this finds you well")
- Clear, well-structured body
- Specific numbers and results where relevant
- Strong call-to-action
- Professional signature for {fr}
- Sound like a real person — confident, direct, no corporate fluff"""
                    r = client.chat.completions.create(model=model, messages=[{"role":"user","content":ep}], temperature=0.3, max_tokens=2000)
                    result = r.choices[0].message.content
                    st.markdown(result)
                    st.divider()
                    st.code(result, language=None)
                    st.download_button("📥 Download", data=result, file_name="email.txt", use_container_width=True)
                    st.session_state.done += 1
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            today = datetime.now().strftime("%B %d, %Y")
            de = f"""## ✉️ Email Draft

---

**Subject:** {sb or f'{et} — Action Required'}
**Date:** {today} | **To:** {to or 'Dear Client'} | **From:** {fr} | **Priority:** {ur}

---

{to or 'Hi there'},

Thank you for taking the time to connect. I wanted to reach out regarding {sb or 'our current collaboration'} and share some important updates with you.

{f'Key areas to cover: {cx}' if cx else 'Here are the main highlights from our recent work together:'}

**Summary:**
- ✅ All deliverables completed ahead of schedule
- ✅ Performance metrics exceeding targets by 23%
- ✅ Team adoption rate at 89% and climbing
- ✅ Projected ROI of 172% in the first year

**Recommended Next Steps:**
1. Schedule a 30-minute review call this week
2. Walk through the detailed results dashboard
3. Discuss Phase 2 scope and timeline

I'd love to find 30 minutes to walk through everything in detail. Would any time this week work for you?

Best regards,

**{fr}**
AI Solutions & Automation
📧 duashaikh@email.com

---
*Connect your API key for fully customized, AI-powered emails.*"""
            st.markdown(de)
            st.code(de, language=None)
            st.download_button("📥 Download", data=de, file_name="email.txt", use_container_width=True)
            st.session_state.done += 1

# ============================================
# TAB 4: REPORT BUILDER
# ============================================
with tab4:
    st.markdown('<div class="stitle">📋 Report Builder</div>', unsafe_allow_html=True)
    
    r1,r2 = st.columns(2)
    with r1:
        rt = st.selectbox("📋 Type:", ["Executive Summary","Market Research","Project Status","Quarterly Review","Competitor Analysis","Financial Overview","Customer Insights","Strategic Plan","Risk Assessment","Team Performance"])
        co = st.text_input("🏢 Company:", placeholder="e.g., IntelliForce AI Solutions")
        pe = st.text_input("📅 Period:", placeholder="e.g., Q1 2026 (Jan — Mar)")
        pb = st.text_input("👤 Prepared By:", value="Dua Shaikh")
    with r2:
        fm = st.selectbox("📄 Format:", ["Executive Brief (1-2 pages)","Standard Report","Detailed Report","Bullet Points","Board Presentation"])
        au = st.selectbox("👥 Audience:", ["CEO / Board","Management","Technical Team","Investors","All Staff"])
        kp = st.text_area("📌 Key Points:", placeholder="Key metrics, achievements, challenges to cover...", height=132)
    
    id = False
    if st.session_state.data is not None:
        id = st.checkbox("📊 Include uploaded data analysis")
    
    if st.button("📋 Generate Report", type="primary", use_container_width=True):
        if client:
            with st.spinner("Building your report..."):
                try:
                    di = ""
                    if id and st.session_state.data is not None:
                        di = f"\n\nAnalyze this data:\nColumns: {list(st.session_state.data.columns)}\nStats:\n{st.session_state.data.describe().to_string()}\nData:\n{st.session_state.data.to_string()}"
                    
                    rp = f"""Create a professional {rt} report in {fm} format.
Company: {co} | Period: {pe} | By: {pb} | Audience: {au}
Key Points: {kp}{di}

Requirements:
- Document header with company, date, prepared by
- Executive summary
- KPIs in table format with specific numbers
- Status indicators (✅ ⚠️ 🔴)
- Trend analysis with comparisons
- Risk assessment
- Prioritized recommendations
- Action items with owners and deadlines
- Boardroom-quality language
- Write as {pb}, the analyst — never mention AI or ChatGPT"""
                    r = client.chat.completions.create(model=model, messages=[{"role":"user","content":rp}], temperature=0.2, max_tokens=4000)
                    result = r.choices[0].message.content
                    st.markdown(result)
                    st.divider()
                    st.download_button("📥 Download Report", data=result, file_name=f"report_{datetime.now():%Y%m%d}.txt", use_container_width=True)
                    st.session_state.done += 1
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            dr = f"""# {rt}

**Company:** {co or 'IntelliForce AI Solutions'}
**Period:** {pe or 'Q1 2026'}
**Prepared By:** {pb}
**Date:** {datetime.now().strftime('%B %d, %Y')}
**Classification:** Confidential — {au}

---

## Executive Summary

This report covers {co or 'business'} performance during {pe or 'Q1 2026'}. The overall trajectory is strong, with revenue exceeding targets and operational metrics showing consistent improvement across all key areas.

**Highlights at a Glance:**
- ✅ Revenue exceeded target by **18%** — reaching $590K against $500K goal
- ✅ Customer base grew **34%** quarter-over-quarter
- ✅ Operating costs reduced **12%** through automation
- ✅ Customer satisfaction improved to **4.7/5.0**
- ⚠️ Two areas flagged for attention — delivery speed and hiring pipeline

---

## Key Performance Indicators

| KPI | Target | Actual | Variance | Status |
|-----|--------|--------|----------|--------|
| Revenue | $500K | $590K | +18% | ✅ Exceeding |
| New Clients | 15 | 21 | +40% | ✅ Exceeding |
| Client Retention | 90% | 94% | +4% | ✅ Strong |
| Profit Margin | 22% | 28% | +6% | ✅ Exceeding |
| On-Time Delivery | 95% | 88% | -7% | ⚠️ Below |
| Team Utilization | 80% | 92% | +12% | ⚠️ High Risk |

---

## Revenue Analysis

| Service Line | Revenue | Share | QoQ Growth |
|-------------|---------|-------|-----------|
| AI Agent Development | $236K | 40% | +45% |
| Document AI / RAG | $148K | 25% | +32% |
| Strategy Consulting | $89K | 15% | +18% |
| Training Programs | $59K | 10% | +28% |
| Support Contracts | $59K | 10% | +12% |

---

## What Went Well

1. **AI Agent services grew 45%** — strongest segment, driven by 6 new deployments
2. **Client retention at 94%** — significantly above the 85% industry average
3. **Average deal size up 22%** — from $18K to $22K per engagement
4. **Referral rate of 35%** — over a third of new business comes from existing clients

## Areas for Improvement

1. **On-time delivery at 88%** — three projects delivered late due to mid-project scope changes
2. **Team utilization at 92%** — unsustainably high, creating burnout risk
3. **Sales pipeline at 2.1x coverage** — below the 3x target needed for predictable growth

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Team burnout | High | High | Hire 2 engineers within 30 days |
| Client concentration | Medium | High | No client should exceed 20% of revenue |
| Technology shifts | Medium | Medium | Allocate 10% of time to R&D |
| Pricing pressure | Low | Medium | Differentiate on quality and speed |

---

## Recommendations

### Immediate — This Month
1. **Hire 2 senior AI engineers** — address capacity constraints before Q2 ramp
2. **Implement scope management process** — prevent future delivery delays

### This Quarter
3. **Launch standardized AI Agent package** — $25K fixed price, faster sales cycle
4. **Expand mid-market outreach** — best unit economics, fastest close rates

### Next Quarter
5. **Build recurring revenue to 30%** — monthly support contracts create stability
6. **Establish 3 strategic partnerships** — co-selling with established consulting firms

---

## Action Items

| Action | Owner | Deadline | Priority |
|--------|-------|----------|----------|
| Leadership review meeting | {pb} | This Week | 🔴 Critical |
| Post 2 engineering positions | HR | 2 Weeks | 🔴 Critical |
| Scope management rollout | PM Lead | 3 Weeks | 🟡 High |
| Mid-market campaign launch | Marketing | 4 Weeks | 🟡 High |
| Partner outreach (3 targets) | BD | 6 Weeks | 🟢 Medium |

---

**Prepared by {pb}**
**{datetime.now().strftime('%B %d, %Y')}**

*Connect your API key for customized reports with real data analysis.*"""
            st.markdown(dr)
            st.divider()
            st.download_button("📥 Download Report", data=dr, file_name=f"report_{datetime.now():%Y%m%d}.txt", use_container_width=True)
            st.session_state.done += 1

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="ft">
    <div class="ft-name">Dua Shaikh</div>
    <p>AI Engineer — Intelligent Systems & Automation</p>
    <p style="margin-top:10px;">
        <a href="https://linkedin.com">LinkedIn</a> &nbsp;·&nbsp;
        <a href="https://github.com">GitHub</a> &nbsp;·&nbsp;
        <a href="mailto:duashaikh@email.com">Email</a>
    </p>
    <p style="margin-top:14px;font-size:0.78rem;color:#4a4672;">
        © 2026 Dua Shaikh — All Rights Reserved
    </p>
</div>
""", unsafe_allow_html=True)