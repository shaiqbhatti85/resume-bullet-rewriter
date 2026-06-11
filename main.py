import streamlit as st
from rewriter import rewrite_bullet
from styles import inject_css

st.set_page_config(
    page_title="Resume Bullet Rewriter",
    page_icon="✦",
    layout="centered",
)

inject_css()

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-block">
    <div class="header-icon">✦</div>
    <div>
        <h1 class="app-title">Resume Bullet Rewriter</h1>
        <p class="app-sub">Paste a weak bullet — get three stronger versions, instantly.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Controls ──────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    role = st.selectbox(
        "Role / Level",
        ["AI / ML Engineer", "Software Engineer", "Data Scientist",
         "Data Engineer", "Backend Engineer", "Frontend Engineer", "Product Manager"],
        index=0,
    )

with col2:
    tone = st.selectbox(
        "Tone / Focus",
        ["Impact-driven (quantified results)", "Technical depth",
         "Leadership & collaboration", "Innovation & problem-solving", "FAANG-optimized"],
        index=0,
    )

# ── Input ─────────────────────────────────────────────────────────────────────
bullet = st.text_area(
    "Your bullet point",
    placeholder="e.g. Worked on ML models to improve recommendations",
    height=110,
)

char_count = len(bullet)
st.markdown(
    f'<p style="text-align:right;font-size:12px;color:#888;margin-top:-10px;">{char_count} chars</p>',
    unsafe_allow_html=True,
)


# ── Rewrite Button ────────────────────────────────────────────────────────────
rewrite_clicked = st.button("✦  Rewrite Bullet", use_container_width=True, type="primary")

if rewrite_clicked:
    if not bullet.strip():
        st.error("Please paste a bullet point first.")
    else:
        with st.spinner("Rewriting with AI..."):
            result = rewrite_bullet(
                bullet=bullet,
                role=role,
                tone=tone
            )

        if result["success"]:
            st.session_state["last_result"] = result["bullets"]
            st.session_state["last_original"] = bullet
        else:
            st.error(f"Error: {result['error']}")

# ── Results ───────────────────────────────────────────────────────────────────
if st.session_state.get("last_result"):
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="original-label">Original</div>'
        f'<div class="original-box">{st.session_state["last_original"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<p class="results-heading">Rewritten versions</p>', unsafe_allow_html=True)

    tags = [("High impact", "tag-impact"), ("Concise", "tag-concise"), ("Technical", "tag-technical")]

    for i, (text, (tag_label, tag_cls)) in enumerate(zip(st.session_state["last_result"], tags)):
        word_count = len(text.split())
        has_metric = any(c.isdigit() for c in text)
        metric_badge = '<span class="meta-badge">📊 Has metrics</span>' if has_metric else ""

        st.markdown(f"""
        <div class="bullet-card">
            <div class="card-top">
                <p class="bullet-text">{text}</p>
                <span class="bullet-tag {tag_cls}">{tag_label}</span>
            </div>
            <div class="card-meta">
                <span class="meta-badge">✦ {word_count} words</span>
                {metric_badge}
                <span class="meta-badge">Variant {i+1} of 3</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.code(text, language=None)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    if st.button("↺  Clear & Start Over", use_container_width=False):
        st.session_state.pop("last_result", None)
        st.session_state.pop("last_original", None)
        st.rerun()
