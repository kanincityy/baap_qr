import streamlit as st
import base64
import os

st.set_page_config(page_title="Tatiana Limonova | BAAP 2026", layout="wide", initial_sidebar_state="collapsed", page_icon="🌟")

# Custom CSS for Academic Poster aesthetics
poster_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* Global settings - aggressively overriding Streamlit containers */
[data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #F4F4F0 !important;
}

div.stApp {
    background-color: #F4F4F0 !important;
    font-family: 'Inter', sans-serif !important;
    color: #1A1A1A !important;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    color: #1A1A1A !important; /* Darkened for readability */
}

/* Typography */
h1, h2, h3 {
    font-weight: 800 !important;
    color: #1A1A1A; /* Darkened for readability */
}

.main-title {
    font-size: 3.5rem !important;
    margin-bottom: 0.5rem !important;
    padding-bottom: 0rem !important;
    line-height: 1.1;
    color: #A82223; /* Standout Info Color */
}

.sub-title {
    font-size: 1.5rem !important;
    font-weight: 600;
    color: #555555;
    margin-bottom: 20px;
}

/* Links / Buttons Base */
.poster-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 20px;
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    color: #FFFFFF !important;
    border-radius: 5px;
    transition: all 0.2s ease;
    margin-right: 0px;
    margin-top: 10px;
    margin-bottom: 20px;
    border: none;
}

.poster-btn:hover {
    transform: translateY(-2px);
}

.btn-linkedin {
    background-color: #0A66C2;
}

.btn-linkedin:hover {
    background-color: #08529C;
    box-shadow: 0px 4px 10px rgba(10, 102, 194, 0.3);
}

.btn-github {
    background-color: #24292e;
}

.btn-github:hover {
    background-color: #1a1e22;
    box-shadow: 0px 4px 10px rgba(36, 41, 46, 0.3);
}

.btn-email {
    background-color: #A82223;
}

.btn-email:hover {
    background-color: #9A1F24;
    box-shadow: 0px 4px 10px rgba(193, 39, 45, 0.3);
}

/* Streamlit Native Download Button Override */
[data-testid="stDownloadButton"] button {
    background-color: #A82223 !important;
    color: #FFFFFF !important;
    border: none !important;
    padding: 12px 30px !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
    font-family: 'Inter', sans-serif !important;
    width: 100% !important;
}

[data-testid="stDownloadButton"] button:hover {
    background-color: #8A1B1C !important;
    transform: translateY(-2px) !important;
    box-shadow: 0px 4px 12px rgba(168, 34, 35, 0.4) !important;
}

/* Download button container */
[data-testid="stDownloadButton"] {
    display: flex;
    justify-content: center;
    margin: 20px 0;
}

/* Containers */
.intro-box {
    background-color: #FFFFFF; /* High contrast on #F4F4F0 */
    border-left: 5px solid #A82223; /* Standout Info Color */
    padding: 20px 25px;
    margin-bottom: 30px;
    font-size: 1.1rem;
    line-height: 1.6;
    border-radius: 0 5px 5px 0;
    color: #333333;
}

/* Images */
.profile-img {
    width: 100%;
    border-radius: 8px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    object-fit: cover;
    margin-bottom: 20px;
    margin-top: 30px; /* Aligns top of photo with the top of the h1 title */
}

.section-header {
    color: #A82223; /* Standout Info Color */
    font-size: 2rem !important;
    border-bottom: 2px solid #E0E0E0;
    padding-bottom: 10px;
    margin-top: 40px;
    margin-bottom: 25px;
    display: inline-block;
}

/* Paper info text */
.paper-info {
    text-align: center;
    color: #7f7f7f;
    font-size: 0.95rem;
    margin-top: 10px;
    margin-bottom: 30px;
}
</style>
"""
st.markdown(poster_css, unsafe_allow_html=True)

# --- Content Variables ---
name = "Tatiana Limonova"
title = "MSc Language Sciences \n\n University College London"
intro_text = "I'm a speech and language researcher specialising in the acoustic-phonetic analysis of emotional speech. My work bridges computational methods and phonetic theory, investigating how noise degrades the subtle articulatory and prosodic cues that encode emotion. I'm particularly interested in developing phonetically-informed approaches to robust speech processing."
linkedin_url = "https://www.linkedin.com/in/tatiana-limonova/"
github_url = "https://github.com/kanincityy"
email_url = "tatianalimonova23@gmail.com"  
profile_img_path = os.path.join("assets", "profile.png")
pdf_path = os.path.join("assets", "article.pdf")

# --- Layout ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    if os.path.exists(profile_img_path):
        import PIL.Image
        import io
        img = PIL.Image.open(profile_img_path)
        
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        img_html = f'<img src="data:image/png;base64,{img_str}" class="profile-img">'
        st.markdown(img_html, unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div class="profile-img" style="height: 400px; background-color: #ccc; display: flex; align-items: center; justify-content: center; font-weight: bold; text-align: center; padding: 20px;">
            [Profile Image Placeholder]<br><br>Place "profile.png" in assets/
        </div>
        ''', unsafe_allow_html=True)
        
with col2:
    st.markdown(f'<h1 class="main-title">{name}</h1>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title" style="white-space: pre-line;">{title}</div>', unsafe_allow_html=True)
    
    # Buttons side by side (compactly below affiliation)
    st.markdown(f'''
        <div style="display: flex; gap: 20px; margin-bottom: 25px;">
            <a href="{linkedin_url}" class="poster-btn btn-linkedin" style="margin: 0; padding: 8px 16px; font-size: 0.95rem;" target="_blank"><i class="fa-brands fa-linkedin" style="margin-right: 6px;"></i> LinkedIn</a>
            <a href="{github_url}" class="poster-btn btn-github" style="margin: 0; padding: 8px 16px; font-size: 0.95rem;" target="_blank"><i class="fa-brands fa-github" style="margin-right: 6px;"></i> GitHub</a>
            <a href="mailto:{email_url}" class="poster-btn btn-email" style="margin: 0; padding: 8px 16px; font-size: 0.95rem;"><i class="fa-solid fa-envelope" style="margin-right: 6px;"></i> Email</a>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'<div class="intro-box">{intro_text}</div>', unsafe_allow_html=True)

# --- PDF Download Section (Compact & Cohesive) ---
# Read the PDF file first
pdf_available = os.path.exists(pdf_path)
if pdf_available:
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

# Create a unified box for the paper section
st.markdown('''
<div style="background-color: #FFFFFF; 
            border-left: 5px solid #A82223; 
            padding: 30px 35px; 
            margin-top: 30px; 
            border-radius: 0 8px 8px 0;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.05);">
    <h2 style="color: #A82223; font-size: 1.8rem; margin-bottom: 15px; margin-top: 0;">
        Conference Paper | BAAP 2026
    </h2>
    <h3 style="color: #2c2c2c; font-size: 1.3rem; margin-bottom: 20px; font-weight: 600; line-height: 1.4;">
        Activation vs. Valence in Noise: Diagnosing the Phonetic Vulnerabilities of an SER System
    </h3>
    <p style="color: #666; font-size: 1rem; margin-bottom: 25px; line-height: 1.6;">
        This paper systematically investigates how Speech Emotion Recognition (SER) systems fail under noise, revealing that models default to predicting "Calm" at café noise levels (5dB SNR), with 81% of Sad samples misclassified, a critical vulnerability for real-world deployment.
    </p>
</div>
''', unsafe_allow_html=True)

# Download button centered below the box
col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])

with col_dl2:
    if pdf_available:
        st.download_button(
            label="📄 Download Research Paper (PDF)",
            data=pdf_bytes,
            file_name="Limonova_BAAP_2026.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        st.markdown(
            '<div class="paper-info">3 pages • PDF • 500 KB</div>',
            unsafe_allow_html=True
        )
    else:
        st.error(f"❌ PDF file not found at: {pdf_path}")
        st.info("Please place your PDF at: **assets/article.pdf**")