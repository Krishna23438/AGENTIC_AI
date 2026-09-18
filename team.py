from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv()

eng_Agent = Agent(name="English Agent", role="You answer questions in English")
chi_Agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
hindi_Agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")

team_leader = Team(
  name="Answer and Translation Team",
  members=[eng_Agent, chi_Agent, hindi_Agent],
  model=Groq(id="openai/gpt-oss-120b"),
  markdown=True,
  show_members_responses=True,
  instructions="""All member agents must respond to answer the query in their specific language.
    Do not route just one agent.
    Output the response of all agents.
    """
)

team_leader.print_response("What is the capital of India?")


# we get the reponse like this ----
# PS C:\Users\Krishna gupta\OneDrive\Desktop\AGENTIC_AI> python team.py
# INFO Agent 'English Agent' inheriting model from Team:                
#      openai/gpt-oss-120b                                              
# INFO Agent 'Chinese Agent' inheriting model from Team:                
#      openai/gpt-oss-120b                                              
# INFO Agent 'Hindi Agent' inheriting model from Team:                  
#      openai/gpt-oss-120b                                              
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ What is the capital of India?                                      ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ English Agent Response ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ The capital of India is New Delhi.                                 ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Chinese Agent Response ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ 印度的首都是新德里。                                               ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Hindi Agent Response ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ नई दिल्ली।                                                            ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Team Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ • delegate_task_to_member(member_id=english-agent, task=Answer the ┃
# ┃ question: 'What is the capital of India?'                          ┃
# ┃   Provide the answer in English. The good result is a concise      ┃
# ┃ statement of the capital.)                                         ┃
# ┃                                                                    ┃
# ┃ • delegate_task_to_member(member_id=chinese-agent,                 ┃
# ┃ task=回答以下问题：'What is the capital of India?'                 ┃
# ┃   用中文提供答案。好的结果是简明的陈述首都。)                      ┃
# ┃                                                                    ┃
# ┃ • delegate_task_to_member(member_id=hindi-agent, task=भारत की राजधानी   ┃
# ┃ क्या है? इस प्रश्न का उत्तर हिंदी में                                          ┃
# ┃   दें। उत्तर संक्षिप्त हो और राजधानी का नाम बताए।)                               ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (7.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ English: The capital of India is New Delhi.                        ┃
# ┃                                                                    ┃
# ┃ 中文 (Chinese): 印度的首都是新德里。                               ┃
# ┃                                                                    ┃
# ┃ हिन्दी (Hindi): नई दिल्ली।                                               ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛