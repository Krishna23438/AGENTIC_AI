from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()


def build_Agent():
  return Agent(
    db = db,
    model=Groq(id="openai/gpt-oss-120b"),
    markdown=True,
    add_history_to_context=True # for short term memory
  )

agent = build_Agent()

agent.print_response("What is the capital of India?")
agent.print_response("Which are the best places to visit it?")

# first install sqlalchemy from sqlalchemy

# responses are :
# PS C:\Users\Krishna gupta\OneDrive\Desktop\AGENTIC_AI> python memory.py
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ What is the capital of India?                                      ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (1.6s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ The capital of India is New Delhi.                                 ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ Which are the best places to visit it?                             ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (3.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                    ┃
# ┃ Top Places to Visit in India 🇮🇳                                    ┃
# ┃                                                                    ┃
# ┃ Below is a curated list of must‑see destinations, grouped by       ┃
# ┃ region and theme. Feel free to mix‑and‑match based on the time you ┃
# ┃ have, your interests, and travel style.                            ┃
# ┃                                                                    ┃
# ┃                                                                    ┃
# ┃                                  Why It’s Worth                    ┃
# ┃  Region          City / Site     a Visit         Highlights        ┃
# ┃  ────────────────────────────────────────────────────────────────  ┃
# ┃  North           Delhi           India’s         Red Fort, Qutub   ┃
# ┃                  (including New  bustling        Minar, India      ┃
# ┃                  Delhi)          capital blends  Gate, Lotus       ┃
# ┃                                  history with    Temple, street    ┃
# ┃                                  modernity.      food in Old       ┃
# ┃                                                  Delhi.            ┃
# ┃                  Agra            Home of the     Taj Mahal, Agra   ┃
# ┃                                  world‑famous    Fort, Mehtab      ┃
# ┃                                  marble          Bagh sunset       ┃
# ┃                                  mausoleum.      view.             ┃
# ┃                  Jaipur          “Pink City” –   Amber Fort, City  ┃
# ┃                  (Rajasthan)     a royal         Palace, Hawa      ┃
# ┃                                  heritage        Mahal, vibrant    ┃
# ┃                                  experience.     bazaars.          ┃
# ┃                  Varanasi        One of the      Ghats & Ganga     ┃
# ┃                  (Uttar          world’s oldest  sunrise,          ┃
# ┃                  Pradesh)        living cities,  Sarnath, silk     ┃
# ┃                                  spiritual       weaving.          ┃
# ┃                                  heart of                          ┃
# ┃                                  Hinduism.                         ┃
# ┃                  Leh‑Ladakh      High‑altitude   Pangong Lake,     ┃
# ┃                  (Jammu &        desert with     Nubra Valley,     ┃
# ┃                  Kashmir)        dramatic        Buddhist          ┃
# ┃                                  mountain        monasteries,      ┃
# ┃                                  scenery.        trekking.         ┃
# ┃  West            Mumbai          India’s         Gateway of        ┃
# ┃                  (Maharashtra)   financial hub   India, Marine     ┃
# ┃                                  & Bollywood     Drive, Elephanta  ┃
# ┃                                  capital.        Caves,            ┃
# ┃                                                  street‑food       ┃
# ┃                                                  stalls.           ┃
# ┃                  Goa             Laid‑back       Baga/Anjuna       ┃
# ┃                                  beaches,        beaches, Old Goa  ┃
# ┃                                  Portuguese      churches, spice   ┃
# ┃                                  heritage,       farms.            ┃
# ┃                                  nightlife.                        ┃
# ┃                  Udaipur         “City of        Lake Pichola      ┃
# ┃                  (Rajasthan)     Lakes” –        boat ride, City   ┃
# ┃                                  romantic        Palace, Jagdish   ┃
# ┃                                  palaces and     Temple.           ┃
# ┃                                  sunsets.                          ┃
# ┃                  Ajanta &        UNESCO World    Magnificent       ┃
# ┃                  Ellora Caves    Heritage        frescoes,         ┃
# ┃                  (Maharashtra)   rock‑cut        intricate         ┃
# ┃                                  Buddhist,       sculptures.       ┃
# ┃                                  Hindu & Jain                      ┃
# ┃                                  temples.                          ┃
# ┃  South           Kerala          Lush greenery,  Alleppey          ┃
# ┃                  (Backwaters &   houseboat       houseboats,       ┃
# ┃                  Hill Stations)  cruises,        Munnar tea        ┃
# ┃                                  Ayurvedic       estates,          ┃
# ┃                                  wellness.       Kumarakom bird    ┃
# ┃                                                  sanctuary.        ┃
# ┃                  Hampi           Ruins of the    Virupaksha        ┃
# ┃                  (Karnataka)     Vijayanagara    Temple, Stone     ┃
# ┃                                  Empire,         Chariot, Sunset   ┃
# ┃                                  surreal         at Matanga Hill.  ┃
# ┃                                  boulder                           ┃
# ┃                                  landscape.                        ┃
# ┃                  Mysore          Royal           Mysore Palace,    ┃
# ┃                  (Karnataka)     heritage,       Chamundi Hill,    ┃
# ┃                                  silk, and       Devaraja Market.  ┃
# ┃                                  sandalwood.                       ┃
# ┃                  Kolkata (West   Cultural        Victoria          ┃
# ┃                  Bengal)         capital,        Memorial, Howrah  ┃
# ┃                                  colonial        Bridge, Kalighat  ┃
# ┃                                  architecture,   Temple, street    ┃
# ┃                                  literary        sweets.           ┃
# ┃                                  history.                          ┃
# ┃                  Pondicherry     French          Promenade Beach,  ┃
# ┃                  (Union          colonial charm  Aurobindo         ┃
# ┃                  Territory)      on the Bay of   Ashram, colorful  ┃
# ┃                                  Bengal.         bougainvillea     ┃
# ┃                                                  streets.          ┃
# ┃  East &          Darjeeling      Tea‑laden       Toy Train ride,   ┃
# ┃  Northeast       (West Bengal)   hills with      Tiger Hill        ┃
# ┃                                  Himalayan       sunrise, tea      ┃
# ┃                                  vistas.         gardens.          ┃
# ┃                  Sikkim          Pristine        Tsomgo Lake,      ┃
# ┃                  (Gangtok &      mountains,      Rumtek            ┃
# ┃                  North‑East)     Buddhist        Monastery,        ┃
# ┃                                  monasteries,    trekking to       ┃
# ┃                                  eco‑tourism.    Goecha La.        ┃
# ┃                  Kaziranga       UNESCO site     Jeep safari,      ┃
# ┃                  National Park   famed for       bird watching,    ┃
# ┃                  (Assam)         one‑horned      elephant rides.   ┃
# ┃                                  rhinoceros.                       ┃
# ┃                  Puri & Konark   Spiritual       Jagannath         ┃
# ┃                  (Odisha)        beach town and  Temple, Sun       ┃
# ┃                                  architectural   Temple at         ┃
# ┃                                  marvel.         Konark, Puri      ┃
# ┃                                                  beach.            ┃
# ┃  Central         Khajuraho       UNESCO temples  Western, Eastern  ┃
# ┃                  (Madhya         with intricate  & Southern        ┃
# ┃                  Pradesh)        erotic          groups of         ┃
# ┃                                  sculptures.     temples.          ┃
# ┃                  Bandhavgarh &   Tiger reserves  Safari drives,    ┃
# ┃                  Kanha National  with rich       birding, tribal   ┃
# ┃                  Parks (Madhya   wildlife.       villages.         ┃
# ┃                  Pradesh)                                          ┃
# ┃                                                                    ┃
# ┃                                                                    ┃
# ┃ Quick‑Pick Itineraries                                             ┃
# ┃                                                                    ┃
# ┃                                                                    ┃
# ┃  Duration              Sample Route          Highlights            ┃
# ┃  ────────────────────────────────────────────────────────────────  ┃
# ┃  7 days (Northern      Delhi → Agra →        Taj Mahal, Amber      ┃
# ┃  Classic)              Jaipur (Golden        Fort, bustling        ┃
# ┃                        Triangle)             bazaars, camel ride.  ┃
# ┃  10 days (South‑Coast  Bangalore → Mysore →  Palaces, tea hills,   ┃
# ┃  & Backwaters)         Ooty → Cochin →       coastal forts,        ┃
# ┃                        Alleppey (houseboat)  backwater cruise.     ┃
# ┃                        → Trivandrum                                ┃
# ┃  12 days (Cultural &   Delhi → Varanasi →    Spiritual rites,      ┃
# ┃  Wildlife)             Khajuraho → Kanha →   UNESCO temples,       ┃
# ┃                        Mumbai → Goa          tiger safari, beach   ┃
# ┃                                              relaxation.           ┃
# ┃  14 days (Adventure &  Delhi → Shimla →      Mountain passes,      ┃
# ┃  Himalayas)            Manali → Leh‑Ladakh   Buddhist              ┃
# ┃                        (Leh‑Pangong‑Nubra)   monasteries,          ┃
# ┃                                              stunning lakes.       ┃
# ┃                                                                    ┃
# ┃                                                                    ┃
# ┃ Travel Tips                                                        ┃
# ┃                                                                    ┃
# ┃  1 Best time to visit –                                            ┃
# ┃     • North & Central: Oct – Mar (cool & dry).                     ┃
# ┃     • South & West Coast: Oct – Feb (pleasant weather).            ┃
# ┃     • Himalayan regions: Apr – Jun & Sep – Oct (clear skies, less  ┃
# ┃       crowds).                                                     ┃
# ┃  2 Getting around –                                                ┃
# ┃     • Domestic flights are cheap and save time for long distances. ┃
# ┃     • Trains (especially the Indian Railways’ premium Rajdhani,    ┃
# ┃       Shatabdi, and Duronto services) offer comfortable overnight  ┃
# ┃       journeys.                                                    ┃
# ┃     • Hiring a car/driver works well for regional circuits (e.g.,  ┃
# ┃       Golden Triangle, Kerala backwaters).                         ┃
# ┃  3 Cultural etiquette –                                            ┃
# ┃     • Dress modestly when visiting temples and mosques.            ┃
# ┃     • Remove shoes before entering religious sites.                ┃
# ┃     • Tipping (10 % in restaurants, INR 50‑200 for guides/drivers) ┃
# ┃       is customary.                                                ┃
# ┃  4 Health & safety –                                               ┃
# ┃     • Stay hydrated; drink bottled or filtered water.              ┃
# ┃     • Carry a basic medical kit (pain relievers, antidiarrheal,    ┃
# ┃       band‑aids).                                                  ┃
# ┃     • Use reputable ride‑hailing apps (Ola, Uber) in major cities. ┃
# ┃                                                                    ┃
# ┃ ------------------------------------------------------------------ ┃
# ┃                                                                    ┃
# ┃ Enjoy your Indian adventure! If you’d like a more detailed         ┃
# ┃ itinerary for a specific region or need suggestions on             ┃
# ┃ accommodation, transport, or local food, just let me know. 🚂🕌🏞️  ┃
# ┃                                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
