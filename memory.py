from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

def build_Agent():
  return Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    markdown=True,
    instructions="",
    add_datetime_to_context=True
  )

agent = build_Agent()

agent.print_response("")