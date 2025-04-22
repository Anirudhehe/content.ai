import streamlit as st
from generator import generate_content
import pyperclip
import datetime
import re

# Set page config (fixed invalid mode param)
st.set_page_config(
    page_title="Content.ai",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for styling and white theme
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background-color: #FFFFFF !important;
    }
    .main {
        background-color: #FFFFFF !important;
    }
    .logo-header {
        font-size: 4rem;
        font-weight: 800;
        color: #2E3192;
        text-align: center;
        padding: 20px 0;
        font-family: Open-sans, sans-serif;
        margin-bottom: 0;
    }
    .input-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef !important;
        padding: 15px;
        font-size: 1.1rem;
        border-radius: 10px;
        color: #131313;
        outline: none !important;
        box-shadow: none !important;
    }
    
    /* Override Streamlit's default focus styles */
    .stTextInput > div > div > input:focus {
        border: 1px solid #e9ecef !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    /* Override Streamlit's base container styles */
    .stTextInput > div {
        border: none !important;
        box-shadow: none !important;
    }
    
    .stTextInput > div:focus-within {
        border: none !important;
        box-shadow: none !important;
    }
    
    .stTextInput > div > div {
        border: none !important;
        box-shadow: none !important;
    }
    .stTextInput > div > div > input:focus {
        border: 1px solid #e9ecef;
        box-shadow: none;
        outline: none;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #666666;
    }
    # .stTextInput > div > div > input:focus {
    #     border-color: #131313;
    #     box-shadow: 0 0 0 0 #131313;
    # }
    .stButton > button {
        width: 100%;
        padding: 10px 20px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
        background-color: #2E3192;
        color: #ffffff;
        border: 1px solid #e0e3e9;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        background-color: #4c4db3;
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
    
    /* Add footer styling */
    .stMarkdown {
        color: #333333 !important;
    }
    
    .element-container:has(> div.stMarkdown > div > p > div > span) {
        color: #333333 !important;
    }
    
    .stMarkdown p {
        color: #333333 !important;
    }
    
    .stText {
        color: #333333 !important;
    }
    .footer-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px;
        background-color: white;
        text-align: center;
        border-top: 1px solid #e9ecef;
    }
    .stSpinner > div > div > div > div {
        color: #333333 !important;
    }
    
    /* Add spinner text color override */
    div[data-testid="stSpinner"] {
        color: #333333 !important;
    }
    
    div[data-testid="stSpinner"] > div {
        color: #333333 !important;
    }
    
    .stSpinner {
        color: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)

# Session state
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ""

if 'count' not in st.session_state:
    st.session_state.count = 0

# Logo and subtitle
st.markdown('<div class="logo-header">CONTENT.ai</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem; color: #666; margin-top:0">Turn any topic into a Blog Post.</p>', unsafe_allow_html=True)

# Input area
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("Blog Topic", placeholder="Type a Topic", label_visibility="collapsed")

with col2:
    generate_button = st.button("Generate", type="primary", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Generate content
if generate_button:
    if not topic:
        st.warning("Please enter a blog topic first.")
    elif len(topic) > 100:
        st.warning("Topic is too long. Please keep it under 100 characters.")
    else:
        with st.spinner("Generating blog post..."):
            st.session_state.generated_text = generate_content(topic)
            st.session_state.count += 1

# Display content
if st.session_state.generated_text:
    st.markdown('<div class="output-section">', unsafe_allow_html=True)

    cleaned_text = re.sub(r'```(?:markdown)?|```', '', st.session_state.generated_text).strip()

    # Estimate read time
    word_count = len(cleaned_text.split())
    read_time = round(word_count / 200)  # 200 words per minute

    # Metadata
    st.markdown("### Your Generated Blog Post")
    st.markdown(f"**🕒 Estimated Read Time:** {read_time} min")
    st.markdown(f"**📅 Generated on:** {datetime.datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    st.markdown("---")
    st.markdown(cleaned_text, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📋 Copy to Clipboard"):
            pyperclip.copy(cleaned_text)
            st.success("✅ Blog post copied to clipboard!")

# Footer
st.markdown('<div class="footer-container">', unsafe_allow_html=True)
st.markdown('<p style="color: #333333; margin: 0;">Made by Anirudh • Posts this session: {}</p>'.format(st.session_state.count), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
