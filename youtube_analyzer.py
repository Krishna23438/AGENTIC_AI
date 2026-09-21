from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.youtube import YouTubeTools

youtube_agent = Agent(
  name="Youtube Agent",
  model=OpenAIResponses(id="gpt-5.2"),
  tools=[YouTubeTools()],
  instructions=dedent("""
    You are an expert Youtube content analyst with a keen eye for detail 
    Follow these steps for comprehensive video analysis:
""")
)