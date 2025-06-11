from crewai import Crew, Process
from agent import (
    researcher,
    strategist,
    writer,
    editor,
    qa_specialist,
    seo_expert,
    summarizer
)
from task import create_tasks
from flask import Flask, request, jsonify, send_from_directory
import os
import time
import hashlib

app = Flask(__name__)

# Store recent inputs to prevent reuse
recent_inputs = {}
INPUT_TIMEOUT = 300  # 5 minutes

def is_input_recent(topic):
    current_time = time.time()
    # Clean up old entries
    recent_inputs.clear()
    
    # Hash the topic for storage
    topic_hash = hashlib.md5(topic.encode()).hexdigest()
    
    if topic_hash in recent_inputs:
        return True
    
    # Store new input
    recent_inputs[topic_hash] = current_time
    return False

# Create the Crew
def create_crew(topic):
    tasks = create_tasks(topic)
    crew = Crew(
        agents=[
            researcher,
            strategist,
            writer,
            editor,
            qa_specialist,
            seo_expert,
            summarizer
        ],
        tasks=tasks,
        verbose=True,
        process=Process.sequential
    )
    return crew

# Serve static files
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

# API endpoint for content generation
@app.route('/generate', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        topic = data.get('topic', '').strip()
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400

        # Check for input reuse
        if is_input_recent(topic):
            return jsonify({
                'error': 'Please wait a few minutes before using the same topic again',
                'message': 'This helps ensure fresh and unique content generation'
            }), 429

        # Create and execute crew
        crew = create_crew(topic)
        result = crew.kickoff()

        if result:
            # Convert CrewOutput to string
            result_str = str(result)
            return jsonify({'result': result_str})
        else:
            return jsonify({'error': 'No result was produced'}), 500

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while generating content'
        }), 500

if __name__ == "__main__":
    # Check if required API keys are set
    required_keys = ['OPENAI_API_KEY', 'SERPER_API_KEY']
    missing_keys = [key for key in required_keys if not os.getenv(key)]
    
    if missing_keys:
        print("Error: Missing required API keys:")
        for key in missing_keys:
            print(f"- {key}")
        print("\nPlease set these keys in your .env file")
        exit(1)

    # Start the Flask server
    app.run(debug=True)
