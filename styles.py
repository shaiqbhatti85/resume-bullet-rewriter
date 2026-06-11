import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Outfit:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    /* ── Global ── */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif !important;
    }
    .stApp {
        background: linear-gradient(
        180deg,
        #020617,
        #08112B,
        #020617);
    }

    .main .block-container {
        max-width: 740px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* ── Header ── */
    .header-block {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 0.5rem;
    }

    .header-icon {
        width: 48px; height: 48px;
        background: #EEEDFE;
        border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        font-size: 22px;
        color: #3C3489;
        flex-shrink: 0;
        border: 1px solid #CEC BF620;
    }

    .app-title {
        font-family: 'DM Serif Display', serif !important;
        font-size: 28px !important;
        font-weight: 400 !important;
        letter-spacing: -0.5px;
        margin: 0 !important;
        color: #FFFFFF !important;
    }

    .app-sub {
        font-size: 14px;
        color: #B8C1EC;
        margin: 3px 0 0 0;
    }

    /* ── Divider ── */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #e0e0e0 20%, #e0e0e0 80%, transparent);
        margin: 1.5rem 0;
    }

    /* ── Original preview ── */
    .original-label {
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: #AAB3D9;
        margin-bottom: 6px;
    }

    .original-box {
        background: #f8f7ff;
        border-left: 3px solid #AFA9EC;
        border-radius: 0 8px 8px 0;
        padding: 10px 14px;
        font-family: 'DM Mono', monospace;
        font-size: 13px;
        color: #444;
        line-height: 1.6;
        margin-bottom: 1.25rem;
    }

    /* ── Results heading ── */
    .results-heading {
        font-size: 12px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: #AAB3D9 !important;
        margin-bottom: 10px !important;
    }

    /* ── Bullet cards ── */
    .bullet-card {
        background: #ffffff;
        border: 1px solid #e8e6f0;
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 10px;
        transition: border-color 0.15s, box-shadow 0.15s;
    }

    .bullet-card:hover {
        background: rgba(15, 23, 42, 0.8);

        border: 1px solid rgba(
        255,
        255,
        255,
        0.1);

        backdrop-filter: blur(12px);

        border-radius: 16px;

        color: white;
    }

    .card-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 10px;
    }

    .bullet-text {
        font-size: 14.5px !important;
        line-height: 1.65 !important;
        color: #1a1a2e !important;
        font-family: 'Outfit', sans-serif !important;
        flex: 1;
        margin: 0 !important;
    }

    .bullet-tag {
        font-size: 11px;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 20px;
        flex-shrink: 0;
        margin-top: 2px;
        white-space: nowrap;
    }

    .tag-impact  { background: #EAF3DE; color: #27500A; }
    .tag-concise { background: #E1F5EE; color: #085041; }
    .tag-technical { background: #E6F1FB; color: #0C447C; }

    .card-meta {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }

    .meta-badge {
        font-size: 11px;
        padding: 2px 8px;
        background: #f4f3fb;
        color: #666;
        border-radius: 4px;
        border: 1px solid #e8e6f0;
    }

    /* ── Streamlit overrides ── */
    .stButton > button {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        transition: all 0.15s !important;
    }

    .stButton > button[kind="primary"] {
            background: linear-gradient(
                90deg,
                #2563EB,
                #7C3AED,
                #C026D3
            ) !important;

            border: none !important;
            color: white !important;

            font-weight: 600 !important;

            height: 55px !important;

            border-radius: 12px !important;
            border-color: #3C3489 !important;
            color: #fff !important;
            font-size: 15px !important;
            padding: 0.6rem 1rem !important;
    }
    .stSelectbox label {
        color: white !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: #534AB7 !important;
        border-color: #534AB7 !important;
    }

    .stTextArea textarea {
        font-family: 'DM Mono', monospace !important;
        font-size: 13px !important;
        border-radius: 8px !important;
        border: 1px solid #e0ddf5 !important;
        background: #101A3D !important;
        color: white !important;
        border: 1px solid #3B82F6 !important;
    }

    .stTextArea textarea:focus {
        border-color: #7F77DD !important;
        box-shadow: 0 0 0 2px rgba(127,119,221,0.15) !important;
    }

    .stSelectbox > div > div {
        border-radius: 8px !important;
        border: 1px solid #e0ddf5 !important;
        background: #101A3D !important;
        color: white !important;
        border: 1px solid #3B82F6 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    .stCode code {
        font-family: 'DM Mono', monospace !important;
        font-size: 13px !important;
        background: #f4f3fb !important;
    }

    /* hide streamlit branding */
    #MainMenu, footer, header { visibility: hidden; }

    .stExpander {
        border: 1px solid #e8e6f0 !important;
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)
