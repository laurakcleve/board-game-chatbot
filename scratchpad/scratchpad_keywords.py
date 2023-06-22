import os
import json
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# keywords = '["word1", "word2"]'


# # print(json.loads(keywords))

# with open("scratchpad_output.json", "w") as f:
#     f.write(json.dumps(json.loads(keywords)))

chunk = "Basic Room action - Emergency Room\nTreat your Wounds: Dress all your Serious Wounds OR Heal 1 of your Dressed Serious Wounds OR Heal all your Light Wounds.\n\nBasic Room action - Evacuation Section A, B\nTry To Enter An Escape Pod: You may perform this Action only if any Escape Pod in Section A is Unlocked and has at least 1 empty space. Make a Noise roll. If any Intruder appears in this Room, your attempt to enter an Escape Pod fails. After resolving your Noise roll, if no Intruder has reached the Room, place your Character in one of the Unlocked Escape Pods of Section A, if there's any free space (each Pod has two places and may accommodate up to 2 Characters). See the Escape Pods section at the end of this Room sheet to determine what happens once the Character has entered a Pod. You cannot enter an Escape Pod if any Intruder is present in its corresponding Evacuation Section Room.\n\nBasic Room action - Fire Control System\nInitiate the Fire Control procedure: Choose any 1 Room. Discard a Fire marker from that Room (if there is one). All the Intruders in that Room run away (in a random direction, determined by drawing an Event card - 1 Event card for each Intruder). Hint: You can use Fire Control Procedure even if there is no Fire marker in the Room to make all the Intruders run away from that Room.\n\nBasic Room action - Generator\nInitiate / stop self-destruct Sequence\nSelf-destruct Sequence: Place 1 Status marker on the first, green space of the Self-Destruct Track. From now on, each time you move the Time marker on the Track, also move the marker on the Self-Destruct Track by 1 space. When any Character stops the Self-Destruct sequence, remove the marker (it will be placed again on the green space if a new sequence starts). When the marker reaches any yellow space on the Self-Destruct Track, the Self-Destruct Sequence cannot be aborted anymore and all Escape Pods are Unlocked instantly (but can be Locked again). When the marker reaches the last space (with the \"skull\" icon), the ship explodes. Note: You cannot start the Self-Destruct when any of the Characters are already hibernating. If a hyperspace jump happens while the Self-Destruct Sequence is active, the ship is still considered destroyed.\n\nBasic Room action - Laboratory\nAnalyse 1 object: This Action may only be performed if one of the following Objects is in the Room (for example carried by the Character): Characters Corpse, Intruder Carcass or Egg. Discover 1 corresponding Intruder Weakness card. The Object is not discarded after Research. You may Drop it for free, though.\n\nBasic Room action - Nest\nTake one Egg: Take 1 Egg token from the Intruder Board. After that, perform a Noise roll. The Egg tokens placed on the Intruder board represent the Eggs in the Nest. When you take (or destroy) Eggs from the Nest, take them from the Intruder board. When there are no more Eggs in the Nest (they have all been carried away or destroyed), the Nest is considered destroyed - place 1 Injury marker in the Nest to represent this. If there is a Fire marker in a Room containing uncarried Eggs, destroy 1 uncarried Egg during the Fire Damage step of the Event Phase. Note: You cannot perform any Search Action in this Room. Destroying Eggs: Whenever your Character is in a Room with any uncarried Eggs (not carried by any Character), you can try to destroy these Eggs. Resolve this Action as a Shoot Action or Melee Attack Action. Each Injury (of any type) destroys 1 Egg. In the case of a Melee Attack Action, the Character does not draw a Contamination card or suffer Wounds if they miss. You can also throw grenades into a Room with uncarried Eggs as if an Intruder were there. A Grenade destroys 2 Eggs, a Molotov Cocktail destroys 1 Egg. After every single attempt to destroy an Egg, you must perform a Noise roll.\n\nBasic Room action - Storage\nSearch for an Item: Draw 2 cards from the Item deck of a chosen color (Red, Yellow or Green). Pick 1 card and put the other at the bottom of the deck.\n\nBasic Room action - Surgery\nPerform a Surgery procedure: Scan all Contamination cards (from your Action deck, hand and Discard). Remove all Infected cards. If you have a Larva on your Character board, remove it. After Scanning, your Character suffers 1 Light Wound and you automatically pass. Shuffle all your Action cards (including those in your hand) and place them in your Action deck. Note: After a Surgery procedure you always pass your round, and your hand is empty until the start of the next turn.\n\nAdditional Rooms \"2\"\nEach game, only 5 randomly chosen Additional Rooms are used, out of the 9 available. These Rooms are indicated by the number \"2\" on their back."

keywords_response = openai.ChatCompletion.create(model="gpt-4", messages=[
    {"role": "user", "content": f"Extract keywords from the following text. Format them as an array of strings.\n\n{chunk}"}
])
keywords = keywords_response["choices"][0]["message"]["content"]

print(keywords)
with open("scratchpad_output_response.json", "w") as f:
    f.write(json.dumps(keywords_response))
with open("scratchpad_output_keywords.json", "w") as f:
    f.write(json.dumps(json.loads(keywords)))
