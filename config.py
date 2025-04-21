import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Generation Parameters
TEMPERATURE = 0.7
MAX_TOKENS = 2048
TOP_P = 0.8
TOP_K = 40