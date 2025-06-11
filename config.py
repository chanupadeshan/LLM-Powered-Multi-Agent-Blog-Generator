import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Initialize Serper Search Tool
search_tool = SerperDevTool(api_key=SERPER_API_KEY)


