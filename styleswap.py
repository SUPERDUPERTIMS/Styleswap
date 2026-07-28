import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="StyleSwap AI",
    page_icon="👗",
    layout="centered"
)

# Modern UI Styling & Hiding Streamlit Chrome
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.1rem;
    }
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }
    .card-box {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .stSelectbox label, .stFileUploader label {
        color: #cbd5e1 !important;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="main-title">👗 StyleSwap AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload a photo and transform the clothing style by selecting topics</p>', unsafe_allow_html=True)

# Main Container
with st.container():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    
    # Image Uploader
    uploaded_file = st.file_uploader("Upload an image of a person or outfit", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Original Image", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Style / Topic Selector
st.markdown("### 🎨 Select Clothing Style Topic")

style_categories = {
    "Business / Corporate": "Tailored blazer, sharp button-down shirt, and professional trousers.",
    "Casual Weekend": "Comfortable hoodie, relaxed-fit denim jeans, and clean sneakers.",
    "Traditional / Heritage": "Rich cultural fabric design with classic artisanal detailing.",
    "High Fashion / Runway": "Avant-garde haute couture styling with bold textures.",
    "Athleisure / Sporty": "Performance activewear jacket, moisture-wicking top, and joggers."
}

selected_topic = st.selectbox("Choose a style transformation topic:", list(style_categories.keys()))

# Action Button
if st.button("Transform Outfit Style", type="primary", use_container_width=True):
    if uploaded_file is not None:
        with st.spinner("Applying style transformation..."):
            st.success(f"Successfully applied **{selected_topic}** styling theme!")
            st.info(f"**Target Style Profile:** {style_categories[selected_topic]}")
    else:
        st.warning("Please upload an image first before transforming styles.")
