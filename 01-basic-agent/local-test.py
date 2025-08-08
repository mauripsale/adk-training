import asyncio

from vertexai.preview import reasoning_engines
from basic_agent.agent import root_agent

async def main():
    app = reasoning_engines.AdkApp(
        agent = root_agent,
        enable_tracing = True,
    )

    user_id = "mauri"

    session = app.create_session(user_id = user_id)

    for event in app.stream_query(
        user_id = user_id,
        session_id = session.id,
        message = "What is the capital of Italy?",
    ):
        print("Local test: " + event["content"]["parts"][0]["text"])

if __name__ == "__main__":
    asyncio.run(main())