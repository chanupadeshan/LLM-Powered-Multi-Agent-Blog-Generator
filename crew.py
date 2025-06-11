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

# Execute the crew in a loop
if __name__ == "__main__":
    print("=" * 50)
    print("CrewAI Content Pipeline")
    print("Type 'stop' to exit.")
    print("=" * 50)

    while True:
        topic = input("\nEnter a topic for content generation:").strip()
        if topic.lower() == "stop":
            print("\nExiting CrewAI pipeline. Goodbye!")
            break

        print(f"\nStarting CrewAI with 7 agents for topic: {topic}")
        print("=" * 50)

        try:
            crew = create_crew(topic)
            result = crew.kickoff()
            print("\n" + "=" * 50)
            print("FINAL RESULT:")
            print("=" * 50)
            print(result)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print("Make sure you have set up your API keys properly:")
            print("- OPENAI_API_KEY for OpenAI")
            print("- GOOGLE_API_KEY for Google Custom Search")
            print("- CUSTOM_SEARCH_ENGINE_ID for Google Custom Search")
