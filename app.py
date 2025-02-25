import streamlit as st
from fastai.vision.all import *
import pathlib
import platform

# Fixing pathlib issue on Windows
if platform.system() == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath

# Set page config
st.set_page_config(
    page_title="Transport Classifier",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown(
    """
    <style>
        .main { background-color: #f4f4f4; }
        h1 { text-align: center; color: #ff5733; }
        .stButton>button { background-color: #ff5733; color: white; font-size: 16px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>🚀 Transport Classification Model</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("About the Model")
st.sidebar.info(
    "This is a machine learning model trained with FastAI to classify different types of transport 🚗🚆🚁🚲."
)
st.sidebar.write("👨‍💻 **Built by:** Yusufbek")
st.sidebar.write("📅 **Last Updated:** 2025")

# File uploader
file = st.file_uploader("📤 Upload an Image", type=['png', 'jpeg', 'gif', 'svg', 'jpg', 'webp'])

# Load model with caching
@st.cache_resource
def load_model():
    return load_learner('transport_model.pkl')

model = load_model()

# Layout: Image on the left, prediction on the right
col1, col2 = st.columns([1, 1])

if file:
    # Open image
    img = PILImage.create(file)

    # Display image
    col1.image(img, caption="🖼️ Uploaded Image", use_container_width=True)

    # Prediction
    pred, pred_id, prob = model.predict(img)

    # Display results beautifully
    col2.markdown(f"<h3 style='color: #ff5733;'>📌 Prediction: {pred}</h3>", unsafe_allow_html=True)
    col2.markdown(f"<h4>🔢 Probability: {prob[pred_id] * 100:.1f}%</h4>", unsafe_allow_html=True)

    # Progress bar for probability
    col2.progress(float(prob[pred_id]))
else:
    st.info("⬆️ Please upload an image to classify.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>🚀 Made with by Yusufbek | Powered by FastAI & Streamlit</p>",
    unsafe_allow_html=True
)
