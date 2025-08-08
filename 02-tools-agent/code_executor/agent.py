from google.adk.agents.llm_agent import Agent

from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    model='gemini-2.5-flash',
    name='code_executor',
    instruction="""You are a calculator agent.
     When given a mathematical expression, write and execute Python code to calculate the result.
    Return only the final numerical result as plain text, without markdown or code blocks.
    """,
    description="""Write and Executes Python code to perform calculations.
    """,
    code_executor=BuiltInCodeExecutor(),
)
