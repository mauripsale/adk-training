from google.adk.agents.llm_agent import Agent
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset
import json

OPENAPI_FILE_SPEC="openapi_weather.json"


with open("./openapi_tool/" + OPENAPI_FILE_SPEC) as f:
    openapi_spec_string = f.read()


# --- Create OpenAPIToolset ---
petstore_toolset = OpenAPIToolset(
    spec_str=openapi_spec_string,
    spec_str_type='json',
)

# --- Agent Definition ---
AGENT_NAME_OPENAPI = "openapi_agent"
GEMINI_MODEL = "gemini-2.5-flash"

root_agent = Agent(
    name=AGENT_NAME_OPENAPI,
    model=GEMINI_MODEL,
    tools=[petstore_toolset], # Pass the list of RestApiTool objects
    instruction='''You are a Pet Store assistant managing pets via an API.
    Use the available tools to fulfill user requests.
    When creating a pet, confirm the details echoed back by the API.
    When listing pets, mention any filters used (like limit or status).
    When showing a pet by ID, state the ID you requested.
    ''',
    description="Manages a Pet Store using tools generated from an OpenAPI spec."
)
