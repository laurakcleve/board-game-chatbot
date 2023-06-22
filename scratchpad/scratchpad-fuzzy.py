import json
from fuzzywuzzy import fuzz

from utils import log


with open("index.json", "r") as file:
    index = json.load(file)

# question = "How do you stop the self destruct sequence?"
question = "What happens when you roll danger on a noise roll?"

# keyword = "Self-destruct Sequence"


def print_all_methods(question, keywords):
    print(f"Ratio: {fuzz.ratio(question, keywords)}")
    print(
        f"Partial Ratio: {fuzz.partial_ratio(question, keywords)}")
    print(
        f"Token Sort Ratio: {fuzz.token_sort_ratio(question, keywords)}")
    print(
        f"Token Set Ratio: {fuzz.token_set_ratio(question, keywords)}")
    print(
        f"Partial Token Sort Ratio: {fuzz.partial_token_sort_ratio(question, keywords)}")
    print(
        f"Partial Token Set Ratio: {fuzz.partial_token_set_ratio(question, keywords)}")


# print_all_methods(question, keywords)

# For 'self-destruct sequence'
# keywords = [
#     "Game Play",
#     "consecutive turns",
#     "end game conditions",
#     "Player Phase",
#     "Event Phase",
#     "Draw Action Cards",
#     "hand size",
#     "discarding pile",
#     "First Player Token",
#     "clockwise order",
#     "Player Rounds",
#     "2 Actions",
#     "pass",
#     "Fire marker",
#     "Light Wound",
#     "Time Track",
#     "Time marker",
#     "Self-Destruct Sequence",
#     "Intruder Attack",
#     "Combat",
#     "Character",
#     "Fire Damage",
#     "Injury",
#     "Resolve Event Card",
#     "Intruder Movement",
#     "Intruder Symbol",
#     "Corridor",
#     "Technical Corridor",
#     "Intruder bag",
#     "Event Effect",
#     "discard pile",
#     "Intruder Bag Development",
#     "Larva",
#     "Adult token",
#     "Creeper",
#     "Breeder token",
#     "Noise roll",
#     "Queen",
#     "Nest Room",
#     "Encounter",
#     "Egg token",
#     "Blank token",
#     "End of the Turn"
# ]
# wrong_keywords = [
#     "Fire Marker",
#     "Characters",
#     "Rooms",
#     "Injuries",
#     "Intruders",
#     "explosion",
#     "ship",
#     "Light Wound",
#     "round",
#     "Actions",
#     "Event Phase",
#     "Fire Damage",
#     "Fire markers",
#     "pool",
#     "Event cards",
#     "Malfunctions",
#     "Room Action",
#     "Search Action",
#     "Malfunction Marker",
#     "integrity",
#     "ship's hull",
#     "Repair Action cards",
#     "Tools Item card",
#     "Nest",
#     "Room Covered In Slime",
#     "Special Rooms",
#     "Hibernatorium",
#     "Cockpit",
#     "Engines",
#     "Malfunction markers",
#     "Computer",
#     "Computer Icon",
#     "Door Token",
#     "Corridors",
#     "Noise markers",
#     "Open",
#     "Closed",
#     "Destroyed",
#     "Intruder movement",
#     "Events",
#     "Actions",
#     "Grenade throwing",
#     "Plasma Torch Item",
#     "Mechanic's Item cards"
# ]
keywords = [
    "Noise Roll",
    "Nemesis decks",
    "ship's machinery",
    "Intruders",
    "Character",
    "Noise die",
    "Noise marker",
    "Corridor",
    "Encounter",
    "Danger",
    "Combat",
    "Technical Corridors",
    "Entrance",
    "Silence",
    "Slime marker",
    "Character board",
    "Event card",
    "Event Phase",
    "Adult Intruder",
    "Intruder tokens",
    "Intruder bag",
    "crew",
    "Mechanic Action deck",
    "Technical Corridor Plans Item card",
    "Door tokens",
    "Injury markers",
    "Exploration token",
    "Clothes Item card",
    "Shower Room Action",
    "Room sheet",
    "Status marker"
]
wrong_keywords = [
    "Rooms",
    "Corridors",
    "Character miniatures",
    "Special Rooms",
    "Hibernatorium",
    "Engines",
    "Cockpit",
    "Escape Pod tokens",
    "Intruder miniatures",
    "Movement Action",
    "neighboring Room",
    "Closed Doors",
    "unexplored",
    "exploration token",
    "NOISE ROLL",
    "Careful Movement",
    "Reconnaissance",
    "Escape rule",
    "Exploration Tokens",
    "Items",
    "Item Counter",
    "Nest",
    "Room Covered in Slime",
    "Special Effect",
    "Silence",
    "Danger",
    "Slime marker",
    "Status marker",
    "Character board",
    "Fire",
    "Fire marker",
    "Malfunction",
    "Malfunction marker",
    "Doors",
    "Door token"
]


# print_all_methods(question, keywords)
print_all_methods(question, wrong_keywords)


# scores = []
# for chunk in index:
#     score = fuzz.ratio(question, chunk["keywords"])
#     scores.append(
#         {"keywords": chunk["keywords"], "score": score, "source": chunk["source"]})


# sorted_scores = sorted(scores, key=lambda d: d["score"], reverse=True)

# log(sorted_scores, 'data/fuzztest_output', 'scores')
