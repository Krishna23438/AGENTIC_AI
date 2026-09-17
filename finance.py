from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def build_agent():
  return Agent(
    model= Groq(id="openai/gpt-oss-120b"),
    tools=[DuckDuckGoTools(),YFinanceTools(all=True)],
    markdown=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    add_datetime_to_context=True

  )

agent = build_agent()

agent.print_response("Share the NVDA stock price and analyst recommendations")