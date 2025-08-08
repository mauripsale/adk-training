from google.adk.agents.llm_agent import Agent

from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.5-flash',
    name='google_search',
    instruction="""
    I can answer your questions by searching the internet. Just ask me anything!
    """,
    description="""Agent to answer questions using Google Search
    """,
    tools=[google_search],
)
