from crewai import Agent, Task, Crew, Process
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

researcher = Agent(
    role="Researcher",
    goal="Research new AI insights",
    backstory="You are an AI Research assistant",
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role="Writer",
    goal="Write compelling and engaging blog posts about AI trends and insights",
    backstory="You are an AI Blog writer who is specialised in writing about AI topics",
    verbose=True,
    allow_delegation=False,
)

task1 = Task(description="Invstigate the latest AI trends", agent=researcher)

task2 = Task(
    description="Write a compelling and enggaing blog post based on the latest AI trends",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()
