import google.generativeai as genai
from config import GOOGLE_API_KEY, TEMPERATURE

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_content(topic):
    try:
        prompt = f"""Write a comprehensive blog post about {topic}.
        The blog post should include:
        - An engaging introduction
        - Why the topic matters
        - Key components and analysis
        - Practical applications
        - A conclusion
        
        Format the content in Markdown. leave a line after ```markdown """

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": TEMPERATURE,
            }
        )
        
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"