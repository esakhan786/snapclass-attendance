import streamlit as st
from src.components.landing_page import (
    landing_styles,
    landing_hero,
    landing_stats,
    landing_teacher_portal,
    landing_student_portal,
    landing_techstack,
    landing_footer,
)


def landing_screen():
    """Full public landing page shown before login."""

    landing_styles()

    # ── 1. Big Hero ───────────────────────────────────
    landing_hero()

    # ── 2. CTA Buttons ────────────────────────────────
    st.markdown(
        "<div class='reveal delay-4' style='text-align:center; margin: 56px 0 32px; font-family: \"Plus Jakarta Sans\", sans-serif;'>"
        "<p style='font-size:1.5rem; font-weight:800; color:#0F172A; margin-bottom:12px; letter-spacing: -0.5px;'>"
        "Enter Your Portal</p>"
        "<p style='font-size:1.05rem; color:#475569;'>Choose whether you are a teacher or a student to continue.</p>"
        "</div>",
        unsafe_allow_html=True
    )
    
    _, c1, c2, _ = st.columns([2, 3, 3, 2])
    with c1:
        if st.button("🎓  Student Portal", use_container_width=True,
                     type="primary", key="land_student"):
            st.session_state["login_type"] = "student"
            st.rerun()
    with c2:
        if st.button("🏫  Teacher Portal", use_container_width=True,
                     type="secondary", key="land_teacher"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    # ── 3. Stats strip ────────────────────────────────
    landing_stats()

    # ── 4. Teacher Portal walkthrough ─────────────────
    landing_teacher_portal()

    # ── 5. Student Portal walkthrough ─────────────────
    landing_student_portal()

    # ── 6. Tech Stack ─────────────────────────────────
    landing_techstack()

    # ── 7. Footer ─────────────────────────────────────
    landing_footer()
