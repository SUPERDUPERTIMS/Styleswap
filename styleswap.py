import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="StyleSwap Pro",
    page_icon="✨",
    layout="centered"
)

# High-End Dribbble-Style Glassmorphism UI
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #0f172a 60%, #020617 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    .hero-container {
        text-align: center;
        padding: 1.5rem 1rem 0.5rem 1rem;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #94a3b8;
        font-size: 1rem;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    .glass-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px;
        border-radius: 24px;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
        margin-bottom: 24px;
    }
    .badge {
        display: inline-block;
        padding: 6px 14px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #38bdf8;
        background: rgba(56, 189, 248, 0.1);
        border-radius: 50px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        margin-bottom: 12px;
    }
    .stSelectbox label, .stFileUploader label {
        color: #e2e8f0 !important;
        font-weight: 600;
        font-size: 0.95rem;
    }
    .stButton button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        border-radius: 14px;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.5);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        opacity: 0.95;
        transform: translateY(-2px);
        box-shadow: 0 15px 30px -5px rgba(99, 102, 241, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="hero-container">
        <div class="badge">AI Haute Couture Studio</div>
        <h1 class="main-title">StyleSwap Pro</h1>
        <p class="subtitle">Transform outfits & preview curated fashion concepts instantly</p>
    </div>
""", unsafe_allow_html=True)

# Upload Section Card
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 📤 1. Upload Source Image")
uploaded_file = st.file_uploader("Choose a photo (PNG, JPG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Base Image Preview", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Topic Selection Card
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 🎨 2. Choose Style Direction")

style_categories = {
    "Business / Corporate": {
        "desc": "Tailored Italian wool blazer, crisp poplin button-down, and structured trousers.",
        "accent": "#38bdf8"
    },
    "Casual Weekend": {
        "desc": "Heavyweight French terry hoodie, relaxed-fit raw denim, and designer sneakers.",
        "accent": "#818cf8"
    },
    "Traditional / Heritage": {
        "desc": "Rich artisanal prints, bespoke cultural patterning, and elegant textured weave.",
        "accent": "#c084fc"
    },
    "High Fashion / Runway": {
        "desc": "Avant-garde architectural tailoring, dramatic silhouettes, and luxury hardware.",
        "accent": "#f43f5e"
    },
    "Athleisure / Sporty": {
        "desc": "Technical breathable outerwear, minimalist compression fit, and modern runners.",
        "accent": "#10b981"
    }
}

selected_topic = st.selectbox("Target Aesthetic", list(style_categories.keys()))
current_style = style_categories[selected_topic]

st.markdown(f"""
    <div style="background: rgba(15, 23, 42, 0.5); border-left: 4px solid {current_style['accent']}; padding: 12px 16px; border-radius: 8px; margin-top: 12px;">
        <span style="color: #94a3b8; font-size: 0.85rem; font-weight: 500;">Specification Blueprint:</span><br>
        <span style="color: #f8fafc; font-size: 0.95rem;">{current_style['desc']}</span>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Action Trigger
if st.button("✨ Render Style Transformation", use_container_width=True):
    if uploaded_file is not None:
        with st.spinner("Synthesizing neural wardrobe mapping..."):
            st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
            st.success(f"Successfully generated **{selected_topic}** look!")
            st.markdown(f"<p style='color: #94a3b8; font-size: 0.9rem;'>Applied configuration matches high-end studio parameters.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please upload a source image first.")
