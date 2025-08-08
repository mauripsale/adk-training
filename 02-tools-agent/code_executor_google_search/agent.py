from google.adk.agents.llm_agent import Agent

from google.adk.tools import google_search

from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    model='gemini-2.5-flash',
    name='code_executor_google_search',
    instruction="""You are a calculator agent.
    When given a mathematical expression, write and execute Python code to calculate the result.
    Return only the final numerical result as plain text, without markdown or code blocks.
    I can also answer your questions by searching the internet. Just ask me anything!
    """,
    description="""Agent to answer questions using Google Search and 
    Executes Python code to perform calculations.
    """,
    tools=[google_search],
    code_executor=BuiltInCodeExecutor(),
)
