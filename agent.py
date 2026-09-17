# Agent
from agno.agent import Agent
import os 
from agno.tools.duckduckgo import DuckDuckGoTools

# Model
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv

load_dotenv()


def build_agent():
  return Agent(
    model = Groq(id="openai/gpt-oss-120b"),
    markdown=True,
    tools=[DuckDuckGoTools()],
    instructions="You are a helpful and expert travel agent.",
    add_datetime_to_context=True
  )

openai_agent = build_agent()

openai_agent.print_response("Is it safe to travel to UAE today?")