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
        margin-bottom: 1rem;
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
st.markdown('<div class="main-header">Content.ai</div>', unsafe_allow_html=True)

# Blog topic input
topic = st.text_input("Enter your blog topic", placeholder="e.g., Artificial Intelligence in Healthcare",label_visibility="visible")

# Generate button with a custom color
generate_button = st.button("Generate", type="primary")

# Function to generate blog post
def generate_blog_post(topic):
    return generate_content(topic)

# Generate blog post when button is clicked
if generate_button:
    if topic:
        with st.spinner("Generating blog post..."):
            st.session_state.generated_text = generate_blog_post(topic)
    else:
        st.warning("Please enter a blog topic first.")

# Display generated content
if st.session_state.generated_text:
    st.markdown("### Generated Blog Post")
    # Remove any leading/trailing backticks and 'markdown' text from the generated content
    cleaned_text = st.session_state.generated_text.replace('```markdown', '').replace('```', '').strip()
    st.markdown(cleaned_text, unsafe_allow_html=True)
    
    # Copy button
    if st.button("Copy to Clipboard"):
        st.success("Blog post copied to clipboard!")

