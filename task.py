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
        3. Set the tone and style
        4. Create a detailed article outline with:
           - Introduction
           - Main sections
           - Key takeaways
           - Conclusion''',
        agent=strategist,
        expected_output="A content strategy outline with detailed article structure"
    )

    writing_task = Task(
        description=f'''Write a comprehensive article about "{topic_input}":
        1. Follow the content structure provided
        2. Write in a clear, engaging style
        3. Include:
           - Compelling introduction
           - Well-structured main sections
           - Supporting evidence and examples
           - Clear transitions between sections
           - Strong conclusion
        4. Format the article with:
           - Clear headings and subheadings
           - Bullet points where appropriate
           - Proper paragraph breaks
           - Engaging opening and closing
        5. Aim for 1000-1500 words''',
        agent=writer,
        expected_output="A well-structured, engaging article with proper formatting"
    )

    editing_task = Task(
        description='''Edit and refine the article:
        1. Check grammar and spelling
        2. Improve flow and readability
        3. Ensure factual accuracy
        4. Verify source citations
        5. Enhance transitions
        6. Format the article with:
           - Consistent heading styles
           - Proper spacing
           - Clear paragraph structure
           - Professional formatting''',
        agent=editor,
        expected_output="A polished article with professional formatting and editorial improvements"
    )

    qa_task = Task(
        description='''Perform comprehensive quality assurance:
        1. Verify content accuracy
        2. Check formatting consistency
        3. Review brand guidelines compliance
        4. Validate all citations
        5. Ensure accessibility standards
        6. Complete QA checklist''',
        agent=qa_specialist,
        expected_output="Approved article with completed QA checklist and corrections"
    )

    seo_task = Task(
        description='''Optimize the article for search engines:
        1. Research and implement keywords
        2. Optimize meta descriptions
        3. Improve heading structure
        4. Enhance internal linking
        5. Optimize image alt text
        6. Ensure mobile responsiveness
        7. Format for web readability''',
        agent=seo_expert,
        expected_output="SEO-optimized article with improved web formatting"
    )

    summary_task = Task(
        description='''Create an executive summary:
        1. Highlight key points
        2. Include main findings
        3. Note important statistics
        4. Summarize recommendations
        5. Format as a concise overview
        6. Keep it clear and engaging''',
        agent=summarizer,
        expected_output="A clear, concise executive summary with proper formatting"
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
