from crewai import Task
from agent import researcher, strategist, writer, editor, qa_specialist, seo_expert, summarizer

def create_tasks(topic_input):
    research_task = Task(
        description=f'''Research the topic of "{topic_input}" thoroughly:
        1. Search and analyze information from the web:
           - Find recent and relevant information
           - Gather key statistics and data
           - Collect expert opinions and analysis
        2. Focus on:
           - Current applications and use cases
           - Benefits and challenges
           - Future trends and statistics
           - Expert opinions and analysis
        3. Provide a structured research report with:
           - Key findings from all sources
           - Supporting data
           - Source citations
           - Areas for further investigation''',
        agent=researcher,
        expected_output="A comprehensive research report with verified information from web sources"
    )

    strategy_task = Task(
        description=f'''Create a content strategy for "{topic_input}":
        1. Based on the research findings, outline:
           - Main topics to cover
           - Key points to emphasize
           - Structure of the content
        2. Define the target audience
        3. Set the tone and style''',
        agent=strategist,
        input=research_task,
        expected_output="A content strategy outline"
    )

    writing_task = Task(
        description=f'''Write an article about "{topic_input}":
        1. Use the research findings and strategy
        2. Write 500-1000 words
        3. Include key points and examples
        4. Make it engaging and informative''',
        agent=writer,
        input=strategy_task,
        expected_output="A draft article"
    )

    editing_task = Task(
        description='''Edit the article:
        1. Check for grammar and spelling
        2. Improve clarity and flow
        3. Ensure accuracy
        4. Make it more engaging''',
        agent=editor,
        input=writing_task,
        expected_output="An edited version of the article"
    )

    qa_task = Task(
        description='''Review the final content:
        1. Check for errors
        2. Verify facts
        3. Ensure consistency
        4. Confirm it meets requirements''',
        agent=qa_specialist,
        input=editing_task,
        expected_output="A quality-checked version of the content"
    )

    seo_task = Task(
        description='''Optimize the content:
        1. Add relevant keywords
        2. Improve headings
        3. Enhance readability
        4. Optimize for search engines''',
        agent=seo_expert,
        input=qa_task,
        expected_output="An SEO-optimized version of the content"
    )

    summary_task = Task(
        description='''Create a brief summary:
        1. Highlight main points
        2. Include key findings
        3. Keep it concise
        4. Make it clear''',
        agent=summarizer,
        input=seo_task,
        expected_output="A brief summary of the content"
    )

    return [
        research_task,
        strategy_task,
        writing_task,
        editing_task,
        qa_task,
        seo_task,
        summary_task
    ]
