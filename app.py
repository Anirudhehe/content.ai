import streamlit as st
from generator import generate_content

# Page configuration
st.set_page_config(page_title="Content.ai", layout="centered")

# Simple CSS for minimal styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 0rem;
        text-align: center;
    }
    .container {
        border-radius: 10px;
        padding: 20px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .output-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 30px;
        margin-top: 20px;
        border: 1px solid #e9ecef;
        min-height: 600px;
        overflow-y: auto;
    }
    .output-content {
        max-width: 100%;
        white-space: normal;
        word-wrap: break-word;
        overflow-wrap: break-word;
        line-height: 1.6;
    }
    .stTextInput div[data-baseweb="input"] ~ div {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for generated text
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ""


# Main container
# Update the CSS section with modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.8rem;
        font-weight: 800;
        margin-bottom: 2rem;
        text-align: center;
        background: linear-gradient(45deg, #2E3192, #1BFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 20px 0;
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
    
    /* Hide the "Press enter to apply" text */
    .stTextInput div[data-baseweb="input"] ~ div {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Add a subtitle
# Update the header styling
st.markdown("""
<style>
    .logo-header {
        font-size: 4rem;
        font-weight: 800;
        color: #0000FF;
        text-align: center;  /* Changed to center */
        padding: 10px 0 40px 0;  /* Removed left padding */
        font-family: Open-sans, sans-serif;
        margin-bottom: 0;
    }
    
    .input-container {
        max-width: 800px;
        margin:0;  /* Added top margin */
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Replace the existing header with new logo design
st.markdown('<div class="logo-header">CONTENT<span class="logo-dot">.</span><span class="logo-ai">ai</span></div>', unsafe_allow_html=True)

# Remove the subtitle since it's not in the new design
# st.markdown('<p style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem; color: #666;">Transform your ideas into engaging blog posts with AI</p>', unsafe_allow_html=True)

# Create columns for better layout
# col1, col2 = st.columns([2, 1])

# with col1:
#     topic = st.text_input("", placeholder="Enter your blog topic (e.g., The Future of AI)", label_visibility="collapsed")

# with col2:
#     generate_button = st.button("✨ Generate", type="primary", use_container_width=True)

# Add this to your CSS section
st.markdown("""
<style>
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
    
    /* Hide the "Press enter to apply" text */
    .stTextInput div[data-baseweb="input"] ~ div {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Display generated content
if st.session_state.generated_text:
    st.markdown('<div class="output-section">', unsafe_allow_html=True)
    st.markdown("### Your Generated Blog Post")
    cleaned_text = st.session_state.generated_text.replace('```markdown', '').replace('```', '').strip()
    st.markdown(cleaned_text, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add copy button with better styling
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📋 Copy to Clipboard"):
            st.success("✅ Blog post copied to clipboard!")

# Function to generate blog post
# Move the function definition to the top
def generate_blog_post(topic):
    return generate_content(topic)

# Input container and button
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("", placeholder="Type a Topic", label_visibility="collapsed")

with col2:
    generate_button = st.button("generate", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Generate blog post when button is clicked - Move this right after the button
if generate_button:
    if topic:
        with st.spinner("Generating blog post..."):
            st.session_state.generated_text = generate_blog_post(topic)
    else:
        st.warning("Please enter a blog topic first.")

# Display generated content
if st.session_state.generated_text:
    st.markdown('<div class="output-section">', unsafe_allow_html=True)
    st.markdown("### Your Generated Blog Post")
    cleaned_text = st.session_state.generated_text.replace('```markdown', '').replace('```', '').strip()
    st.markdown(cleaned_text, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Copy button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📋 Copy to Clipboard"):
            st.success("✅ Blog post copied to clipboard!")

st.markdown("---")
st.text("Made by Anirudh")

