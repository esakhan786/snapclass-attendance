import streamlit as st
from PIL import Image

# ─── Mockup image paths ───────────────────────────────────────────────────────
IMGS = {
    "teacher_login":    "C:/Users/DELL/.gemini/antigravity-ide/brain/81a8e50a-3239-45fc-a75a-80a0210e65e0/.user_uploaded/media_1791644632812.png",
    "teacher_register": "C:/Users/DELL/.gemini/antigravity-ide/brain/81a8e50a-3239-45fc-a75a-80a0210e65e0/.user_uploaded/media_1791644658480.png",
    "teacher_dashboard":"C:/Users/DELL/.gemini/antigravity-ide/brain/81a8e50a-3239-45fc-a75a-80a0210e65e0/.user_uploaded/media_1791644711196.png",
    "teacher_subjects": "C:/Users/DELL/.gemini/antigravity-ide/brain/81a8e50a-3239-45fc-a75a-80a0210e65e0/.user_uploaded/media_1791644759321.png",
    "student_faceid":   "C:/Users/DELL/.gemini/antigravity-ide/brain/81a8e50a-3239-45fc-a75a-80a0210e65e0/.user_uploaded/media_1791644871858.png",
    "student_register": "C:/Users/DELL/.gemini/antigravity-ide/brain/81a8e50a-3239-45fc-a75a-80a0210e65e0/.user_uploaded/media_1791646392676.png",
    "student_dashboard":"C:/Users/DELL/.gemini/antigravity-ide/brain/81a8e50a-3239-45fc-a75a-80a0210e65e0/.user_uploaded/media_1791645629406.png",
}


def _bullet_html(items, accent):
    """Build bullet list HTML with no nested f-strings."""
    html = ""
    for item in items:
        html += (
            "<div style='display:flex;align-items:flex-start;gap:10px;margin-top:10px;'>"
            "<span style='width:7px;height:7px;border-radius:50%;background:" + accent + ";"
            "margin-top:6px;flex-shrink:0;display:inline-block;'></span>"
            "<span style='font-family:Outfit,sans-serif;font-size:0.9rem;"
            "color:#475569;line-height:1.65;'>" + item + "</span>"
            "</div>"
        )
    return html


def _step(step_num, icon, title, body, bullets, img_key, accent, reverse=False):
    """Two-column step: [text | image] or [image | text]."""
    bullet_html = _bullet_html(bullets, accent)

    text_html = (
        "<div style='padding:24px 0;'>"
        "<p style='font-family:Outfit,sans-serif;font-size:0.75rem;font-weight:800;"
        "letter-spacing:2.5px;text-transform:uppercase;color:" + accent + ";margin:0 0 10px;'>"
        + step_num + "</p>"
        "<p style='font-family:\"Lilita One\", cursive;font-size:1.65rem;"
        "color:#0F172A;margin:0 0 14px;line-height:1.3;'>"
        + icon + " " + title + "</p>"
        "<p style='font-family:Outfit,sans-serif;font-size:1.05rem;"
        "color:#475569;line-height:1.75;margin:0;'>" + body + "</p>"
        + bullet_html +
        "</div>"
    )

    if reverse:
        c_img, c_txt = st.columns([1, 1], gap="large")
    else:
        c_txt, c_img = st.columns([1, 1], gap="large")

    with c_txt:
        st.markdown(text_html, unsafe_allow_html=True)
    with c_img:
        st.image(Image.open(IMGS[img_key]), width="stretch")


def _divider():
    st.markdown(
        "<hr style='border:none;border-top:1px solid #E2E8F0;margin:48px 0;'>",
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────────────────────────────────────
def landing_styles():
    st.markdown("""
        <style>
        /* ── Reset ── */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            max-width: 980px !important;
        }

        /* ── App background: white ── */
        .stApp { background: #FFFFFF !important; }

        /* ── Buttons ── */
        .stButton button {
            font-weight: 800 !important;
            font-size: 1.05rem !important;
            border-radius: 12px !important;
            padding: 16px 36px !important;
            border: 2px solid transparent !important;
            letter-spacing: 0.5px !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            text-transform: uppercase;
        }
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, #1E3A8A, #3B82F6) !important;
            color: #fff !important;
            box-shadow: 0 8px 24px rgba(30, 58, 138, 0.35) !important;
        }
        .stButton button[kind="primary"]:hover {
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 0 14px 32px rgba(30, 58, 138, 0.5) !important;
            background: linear-gradient(135deg, #1E40AF, #2563EB) !important;
        }
        .stButton button[kind="secondary"] {
            background: #FFFFFF !important;
            color: #1E3A8A !important;
            border: 2px solid #1E3A8A !important;
            box-shadow: 0 6px 16px rgba(0,0,0,0.06) !important;
        }
        .stButton button[kind="secondary"]:hover {
            transform: translateY(-4px) !important;
            background: #EFF6FF !important;
            box-shadow: 0 10px 24px rgba(30, 58, 138, 0.15) !important;
        }

        /* ── Animations ── */
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(24px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes floatBadge {
            0%,100% { transform: translateY(0px); }
            50%      { transform: translateY(-6px); }
        }
        @keyframes gradientShift {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes scalePulse {
            0%,100% { transform: scale(1); }
            50%      { transform: scale(1.06); }
        }
        @keyframes dotBlink {
            0%,100% { opacity: 1; }
            50%      { opacity: 0.3; }
        }

        .fade-up   { animation: fadeUp 0.7s ease both; }
        .fade-up-2 { animation: fadeUp 0.7s ease 0.15s both; }
        .fade-up-3 { animation: fadeUp 0.7s ease 0.3s both; }

        /* ── Stat cards ── */
        .stat-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 22px 20px;
            text-align: center;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }
        .stat-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(0,0,0,0.08);
        }

        /* ── Step image frame ── */
        .stImage img {
            border-radius: 16px !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 12px 36px rgba(0,0,0,0.12), 0 4px 12px rgba(0,0,0,0.06) !important;
            transition: transform 0.35s ease, box-shadow 0.35s ease !important;
        }
        .stImage img:hover {
            transform: translateY(-6px) scale(1.02) !important;
            box-shadow: 0 20px 52px rgba(0,0,0,0.18), 0 8px 16px rgba(79,70,229,0.15) !important;
        }

        /* ── Tech pills ── */
        .tech-pill {
            display: inline-flex; align-items: center; gap: 6px;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.82rem; font-weight: 600;
            color: #475569;
            background: #F1F5F9;
            border: 1px solid #E2E8F0;
            border-radius: 100px;
            padding: 7px 16px;
            transition: background 0.2s ease, transform 0.2s ease;
        }
        .tech-pill:hover {
            background: #EEF2FF;
            color: #4F46E5;
            transform: scale(1.05);
        }

        /* ── Portal section ── */
        .portal-badge {
            display: inline-block;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.7rem; font-weight: 800;
            letter-spacing: 2px; text-transform: uppercase;
            padding: 5px 14px; border-radius: 100px;
        }
        </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
def landing_hero():
    st.markdown(
        "<style>"
        "@import url('https://fonts.googleapis.com/css2?family=Lilita+One&display=swap');"
        ".live-badge {"
        "  display: inline-flex; align-items: center; gap: 8px;"
        "  background: #FFFBEB; border: 1px solid #FCD34D;"
        "  border-radius: 100px; padding: 6px 18px;"
        "  font-family: 'Plus Jakarta Sans', sans-serif;"
        "  font-size: 0.85rem; font-weight: 800;"
        "  color: #B45309; letter-spacing: 1px; text-transform: uppercase;"
        "  margin-bottom: 24px;"
        "  animation: floatBadge 3.5s ease-in-out infinite;"
        "}"
        ".live-dot {"
        "  width: 8px; height: 8px; border-radius: 50%;"
        "  background: #D97706; display: inline-block;"
        "  animation: dotBlink 1.6s ease-in-out infinite;"
        "}"
        ".hero-title {"
        "  font-family: 'Lilita One', cursive !important;"
        "  font-size: clamp(3.5rem, 8vw, 6.5rem) !important;"
        "  color: #0F172A;"
        "  line-height: 1.15 !important;"
        "  margin: 0 0 24px !important;"
        "  letter-spacing: 1px;"
        "}"
        ".hero-title .hl {"
        "  background: linear-gradient(135deg, #4F46E5, #EC4899, #F59E0B);"
        "  background-size: 200% 200%;"
        "  -webkit-background-clip: text; -webkit-text-fill-color: transparent;"
        "  background-clip: text;"
        "  animation: gradientShift 4s ease infinite;"
        "}"
        ".hero-sub {"
        "  font-family: 'Plus Jakarta Sans', sans-serif;"
        "  font-size: clamp(1.1rem, 2.5vw, 1.3rem);"
        "  color: #475569; max-width: 800px;"
        "  font-weight: 500;"
        "  margin: 0 auto 30px;"
        "  line-height: 1.8;"
        "  text-align: center;"
        "}"
        "</style>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='text-align:center;padding: 80px 0 20px;'>"
        "<span class='live-badge'>"
        "<span class='live-dot'></span>"
        "AI-Powered Face & Voice Recognition"
        "</span>"
        "<h1 class='hero-title fade-up'>"
        "Seamless Attendance<br/><span class='hl'>in 10 Seconds.</span>"
        "</h1>"
        "<p class='hero-sub fade-up-2'>"
        "SnapClass automates your entire classroom workflow. One photo marks your students present. If the face scan misses someone, our built-in Voice Attendance catches them as a fallback."
        "</p>"
        "</div>",
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────────────────────────────────────
def landing_stats():
    st.markdown(
        "<div style='display:flex;flex-wrap:wrap;gap:14px;justify-content:center;"
        "padding:0 0 56px;' class='fade-up-3'>",
        unsafe_allow_html=True
    )

    stats = [
        ("~10s",  "Full attendance marked",          "#4F46E5"),
        ("100%",  "Automated — zero manual entry",   "#EC4899"),
        ("2×",    "Verification: face + voice",      "#059669"),
        ("∞",     "Students per class",              "#D97706"),
    ]

    cols = st.columns(4, gap="small")
    for col, (num, label, color) in zip(cols, stats):
        with col:
            st.markdown(
                "<div class='stat-card'>"
                "<p style='font-family:Plus Jakarta Sans,sans-serif;font-size:2rem;"
                "font-weight:900;color:" + color + ";margin:0 0 4px;line-height:1;'>"
                + num + "</p>"
                "<p style='font-family:Plus Jakarta Sans,sans-serif;font-size:0.75rem;"
                "color:#94A3B8;margin:0;font-weight:500;'>" + label + "</p>"
                "</div>",
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
def _portal_header(eyebrow, badge_text, badge_bg, badge_color, title, desc):
    st.markdown(
        "<div style='padding:60px 0 0;text-align:center;'>"
        "<p style='font-family:Plus Jakarta Sans,sans-serif;font-size:0.68rem;"
        "font-weight:800;letter-spacing:3px;text-transform:uppercase;"
        "color:#94A3B8;margin-bottom:14px;'>" + eyebrow + "</p>"
        "<span class='portal-badge' style='background:" + badge_bg + ";color:" + badge_color + ";'>"
        + badge_text + "</span>"
        "<h2 style='font-family:\"Lilita One\", cursive;"
        "font-size:clamp(1.8rem,4vw,2.8rem);"
        "color:#0F172A;margin:12px 0 14px;letter-spacing:0.5px;'>" + title + "</h2>"
        "<p style='font-family:Plus Jakarta Sans,sans-serif;font-size:0.95rem;"
        "color:#64748B;max-width:500px;margin:0 auto 48px;line-height:1.75;'>"
        + desc + "</p>"
        "</div>",
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────────────────────────────────────
def landing_teacher_portal():
    _portal_header(
        eyebrow="✦  Teacher Portal",
        badge_text="For Teachers",
        badge_bg="#EEF2FF",
        badge_color="#4338CA",
        title="Run Your Classroom with AI",
        desc="Create subjects, manage students, and automate attendance. AI handles the heavy lifting, and voice processing provides a seamless fallback."
    )

    _step(
        step_num="Step 01 · Sign Up",
        icon="📝", title="Create Your Profile",
        body="New to SnapClass? Register in seconds — just pick a username, enter your name, and set a password.",
        bullets=[
            "Choose a unique username",
            "Enter your display name and password",
        ],
        img_key="teacher_register", accent="#4F46E5", reverse=False
    )

    _divider()

    _step(
        step_num="Step 02 · Sign In",
        icon="🔐", title="Secure Access",
        body="Teachers sign in securely with a username and password. Quick, private, no email required.",
        bullets=[
            "Enter username and password to log in instantly",
            "Don't have an account? Click <em>Register Instead</em>",
        ],
        img_key="teacher_login", accent="#4F46E5", reverse=True
    )

    _divider()

    _step(
        step_num="Step 03 · Manage Subjects",
        icon="📚", title="Create & Share Courses",
        body="Create a subject for each class. Each gets a unique join code that students can use to enroll.",
        bullets=[
            "Set a subject name, code, and section",
            "Share the join code for immediate enrollment",
        ],
        img_key="teacher_subjects", accent="#4F46E5", reverse=False
    )

    _divider()

    _step(
        step_num="Step 04 · Take Attendance",
        icon="📸", title="Face AI & Voice Fallback",
        body="Upload classroom photos and let AI scan the faces. If any faces fail to be detected, you can open the Voice Attendance fallback to verify students by their voice.",
        bullets=[
            "Upload multiple class photos for better accuracy",
            "Run Face Analysis to mark students present",
            "Use the Voice Attendance fallback if faces aren't recognized",
        ],
        img_key="teacher_dashboard", accent="#7C3AED", reverse=True
    )


# ─────────────────────────────────────────────────────────────────────────────
def landing_student_portal():
    st.markdown(
        "<hr style='border:none;border-top:1px solid #E2E8F0;margin:56px 0;'>",
        unsafe_allow_html=True
    )

    _portal_header(
        eyebrow="✦  Student Portal",
        badge_text="For Students",
        badge_bg="#FDF2F8",
        badge_color="#9D174D",
        title="Your Identity is Your Password",
        desc="Students log in with their face. If your face isn't recognized, simply enroll a new profile and optionally add a voice sample for the teacher's fallback."
    )

    _step(
        step_num="Step 01 · Login",
        icon="🤳", title="FaceID Authentication",
        body="Look into the camera to log in. If your face isn't recognized or the scan fails, you'll be prompted to create a new profile instantly.",
        bullets=[
            "Face detected automatically via webcam",
            "Instant passwordless entry if recognized",
            "Failsafe: Fall back to profile creation if face not found",
        ],
        img_key="student_faceid", accent="#EC4899", reverse=False
    )

    _divider()

    _step(
        step_num="Step 02 · Registration",
        icon="🎓", title="Create Profile & Voice Model",
        body="If you aren't recognized, just type your name. Your face is captured, and you can record a short audio clip so teachers can verify you by voice later.",
        bullets=[
            "Face photo captured automatically",
            "Record a short audio phrase for the voice fallback",
            "No manual uploads required",
        ],
        img_key="student_register", accent="#EC4899", reverse=True
    )

    _divider()

    _step(
        step_num="Step 03 · Dashboard",
        icon="📊", title="Track & Manage Enrollments",
        body="See all your enrolled subjects alongside attendance stats. Join new classes instantly with a code or drop out at any time.",
        bullets=[
            "Monitor your attendance records in real-time",
            "Enroll in new subjects using a join code",
            "Unenroll dynamically with one click",
        ],
        img_key="student_dashboard", accent="#EC4899", reverse=False
    )


# ─────────────────────────────────────────────────────────────────────────────
def landing_techstack():
    pills = [
        ("🐍", "Python"), ("⚡", "Streamlit"), ("🧠", "dlib + face_recognition"),
        ("🎤", "Resemblyzer"), ("🗄️", "Supabase"), ("🔢", "scikit-learn"),
        ("📷", "Pillow"), ("🎵", "Librosa"), ("🔢", "NumPy"), ("🐼", "Pandas"),
    ]
    pill_html = ""
    for emoji, name in pills:
        pill_html += (
            "<span class='tech-pill'>" + emoji + " " + name + "</span>"
        )

    st.markdown(
        "<hr style='border:none;border-top:1px solid #E2E8F0;margin:56px 0 40px;'>"
        "<div style='text-align:center;padding:0 0 16px;'>"
        "<p style='font-family:Plus Jakarta Sans,sans-serif;font-size:0.68rem;"
        "font-weight:800;letter-spacing:3px;text-transform:uppercase;"
        "color:#CBD5E1;margin-bottom:20px;'>BUILT WITH TRUSTED TECHNOLOGIES</p>"
        "<div style='display:flex;flex-wrap:wrap;gap:10px;justify-content:center;'>"
        + pill_html +
        "</div></div>",
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────────────────────────────────────
def landing_footer():
    st.markdown(
        "<hr style='border:none;border-top:1px solid #E2E8F0;margin:56px 0 0;'>"
        "<div style='padding:44px 24px 40px;text-align:center;'>"
        "<p style='font-family:Plus Jakarta Sans,sans-serif;font-size:1.3rem;"
        "font-weight:900;color:#0F172A;letter-spacing:1px;margin-bottom:10px;'>"
        "SNAP<span style='color:#4F46E5;'>CLASS</span></p>"
        "<div style='width:36px;height:3px;"
        "background:linear-gradient(90deg,#4F46E5,#EC4899);"
        "margin:0 auto 16px;border-radius:4px;'></div>"
        "<p style='font-family:Plus Jakarta Sans,sans-serif;font-size:0.82rem;"
        "color:#94A3B8;line-height:1.7;'>"
        "Attendance in 10 seconds — powered by Face AI &amp; Voice Recognition.<br/>"
        "Built with ❤️ using Python &middot; Streamlit &middot; Supabase"
        "</p></div>",
        unsafe_allow_html=True
    )
