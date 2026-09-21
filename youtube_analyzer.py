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
    1. Video Overview
       - Check video length and basic metadata
       - Identity video type (tutorial, review, lecture, etc.)
       - Note the content structure
    2. Timestamp  Creation
      - Create precise, meaningful timestamps
      - Focus on major topic transitions
      - Highlight key moments and demonstrations
      - Format: [start_time, end_time, detailes_summary]

""")
)