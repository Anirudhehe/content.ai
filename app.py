import streamlit as st
from generator import generate_content
import pyperclip

# Page configuration
st.set_page_config(page_title="Content.ai", layout="centered")

# CSS Styling
st.markdown("""
<style>
    .logo-header {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(45deg, #2E3192, #1BFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px 0;
        font-family: Open-sans, sans-serif;
        margin-bottom: 2rem;
    }
    .input-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        padding: 15px;
        font-size: 1.1rem;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #131313;
        box-shadow: 0 0 0 2px #131313;
    }
    .stButton > button {
        width: 100%;
        padding: 10px 20px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
        background-color: #f0f2f6;
        color: #262730;
        border: 1px solid #e0e3e9;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        background-color: #e6e9ef;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    .output-section {
        background: white;
        border-radius: 15px;
        padding: 30px;
        margin-top: 30px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    .output-section h3 {
        color: #2E3192;
        font-size: 1.5rem;
        margin-bottom: 20px;
        border-bottom: 2px solid #e9ecef;
        padding-bottom: 10px;
    }
    .stTextInput div[data-baseweb="input"] ~ div {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Session state for output
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ""

# Logo Header
st.markdown('<div class="logo-header">CONTENT.ai</div>', unsafe_allow_html=True)

# Input Area
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("", placeholder="Type a Topic", label_visibility="collapsed")

with col2:
    generate_button = st.button("✨ Generate", type="primary", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Generate Content
if generate_button:
    if topic:
        with st.spinner("Generating blog post..."):
            st.session_state.generated_text = generate_content(topic)
    else:
        st.warning("Please enter a blog topic first.")

# Display Output
if st.session_state.generated_text:
    st.markdown('<div class="output-section">', unsafe_allow_html=True)
    st.markdown("### Your Generated Blog Post")
    cleaned_text = st.session_state.generated_text.replace('```markdown', '').replace('```', '').strip()
    st.markdown(cleaned_text, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📋 Copy to Clipboard"):
            pyperclip.copy(cleaned_text)
            st.success("✅ Blog post copied to clipboard!")

# Footer
st.markdown("---")
st.text("Made by Anirudh")
