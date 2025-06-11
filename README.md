# CrewAI Content Pipeline - Agentic AI Project

A multi-agent AI system that generates high-quality content through a collaborative workflow of specialized AI agents. This project demonstrates the power of agentic AI by coordinating multiple agents to work together on content creation tasks.

## 🎯 Features

- **Multi-Agent Collaboration**: 7 specialized AI agents working together:
  - Research Specialist: Gathers and analyzes information
  - Content Strategist: Develops content strategy
  - Content Writer: Creates engaging content
  - Content Editor: Polishes and refines content
  - QA Specialist: Ensures quality and accuracy
  - SEO Expert: Optimizes for search engines
  - Executive Summarizer: Creates concise summaries

- **Modern Web Interface**:
  - Real-time progress tracking
  - Interactive agent status updates
  - Clean and responsive design
  - Instant content generation

- **Powerful Tools**:
  - Serper Search integration for web research
  - OpenAI GPT-3.5 Turbo for intelligent content generation
  - Flask backend for reliable API handling

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Serper API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd crewai-content-pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serper_key
```

### Running the Application

1. Start the server:
```bash
python crew.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## 🏗️ Project Structure

```
├── agent.py          # Agent definitions and configurations
├── config.py         # API keys and tool configurations
├── crew.py           # Main application and web server
├── task.py           # Task definitions for each agent
├── tools.py          # Tool definitions and configurations
├── index.html        # Web interface
├── style.css         # Styling for web interface
└── requirements.txt  # Project dependencies
```

## 🤖 Agent System

The project uses a sophisticated agent system where each agent has specific roles and capabilities:

1. **Research Specialist**
   - Uses search tools to gather information
   - Analyzes and validates data
   - Provides comprehensive research reports

2. **Content Strategist**
   - Develops content strategy
   - Defines target audience
   - Creates content outlines

3. **Content Writer**
   - Writes engaging content
   - Follows strategy guidelines
   - Maintains consistent tone

4. **Content Editor**
   - Improves grammar and flow
   - Ensures consistency
   - Enhances readability

5. **QA Specialist**
   - Verifies accuracy
   - Checks compliance
   - Ensures quality standards

6. **SEO Expert**
   - Optimizes for search engines
   - Implements keywords
   - Improves visibility

7. **Executive Summarizer**
   - Creates concise summaries
   - Highlights key points
   - Maintains clarity

## 🔧 Configuration

The system uses the following key configurations:

- **LLM Configuration** (in agent.py):
  ```python
  llm = ChatOpenAI(
      model="gpt-3.5-turbo",
      temperature=0.1,
      max_tokens=1000,
      streaming=True,
      verbose=True
  )
  ```

- **API Keys** (in .env):
  ```
  OPENAI_API_KEY=your_openai_key
  SERPER_API_KEY=your_serper_key
  ```

## 📝 Usage

1. Enter your topic in the web interface
2. Click "Generate Content"
3. Watch the agents work in real-time
4. Receive the final generated content

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- CrewAI for the agent framework
- OpenAI for the language model
- Serper for search capabilities
