import random
from slyfox import slyfox
from grumpy_bull import grumpy_bull

random.seed()

print('''
*******************************************************************************
   ___,,___
           _,-='=- =-  -`"--.__,,.._
        ,-;// /  - -       -   -= - "=.
      ,'///    -     -   -   =  - ==-=\`.
     |/// /  =    `. - =   == - =.=_,,._ `=/|
    ///    -   -    \  - - = ,ndDMHHMM/\b  \\
  ,' - / /        / /\ =  - /MM(,,._`YQMML  `|
 <_,=^Kkm / / / / ///H|wnWWdMKKK#""-;. `"0\  |
        `""QkmmmmmnWMMM\""WHMKKMM\   `--. \> \
              `""'  `->>>    ``WHMb,.    `-_<@)
                                `"QMM`.
                                   `>>>
*******************************************************************************
''')
print("Welcome to Badgerland. You are playing as Scrumpy, the cider-loving badger.\n")
print("Your mission is to find a large crop of apples to make cider from whilst avoiding various pitfalls.\n")
print("Best of luck.\n")

def did_not_enter(requested):
    requested = requested
    print(
        f"You did not state {requested} as requested. You do not have what it takes for the challenging and noble pursuit of badger cider-hunting.\n GAME OVER")

def validate_input(choices, user_input):
    if user_input.lower() not in choices:
        return False
    return True

def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)

def urethral_insertion(num):
    adverbs = ["swiftly", "skillfully", "passionately", "deftly", "suddenly", "smoothly", "quickly", "intensely"]
    verbs = ["pitched", "rammed", "crushed", "drove", "hammered", "packed", "slid", "manouvered", "pumped"]
    adjectives = ["rotten", "stinking", "spikey", "semi-fermented", "massive", "fly-infested", "dripping", "mouldy", "glowing", "humongous", "infected", "oddly-purple"]
    objects = ["apple", "pear", "pineapple", "ugly fruit", "butternut squash", "pile of hay", "worn out tractor wheel", "largest pumpkin ever grown", "particularly foul smelling jackfruit", "kiwi fruit", "custard apple", "ridiculously spiky lychee"]
    adverb = random.choice(adverbs)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    tobject = random.choice(objects)
    pronoun = "it"
    if num != 1:
        tobject += "s"
        pronoun = "them"
    return f"Fiendish Hog takes {num} {adjective} {tobject} and {adverb} {verb} {pronoun} at your face."

def urethral_sensation(num):
    if num < 0:
        return (True, "You feel overwhelmed by the stench of rotten fruit. You collapse to your badger-knees.")
    elif num == 0:
        return (False, "You feel nothing.")
    elif num < 10:
        return (False, "You feel a light tickling sensation in your nose.")
    elif num < 100:
        return (False, "You feel a slight stinging sensation from your nose.")
    elif num < 1000:
        return (False, "You feel a more intense bulging sensation around your nose.")
    elif num < 10000:
        return (False, "You start to feel your fur clump up, mulch sticking it all together.")
    elif num < 100000:
        return (False, "You gag at the stench.")
    elif num < 1000000:
        return (False, "You retch at the stench.")
    elif num < 10000000:
        return (False, "The smell overpowers you. You struggle to see or think because of the intense reek.")
    elif num < 100000000:
        return (False, "You roll on the floor in confused panic.")
    elif num < 1000000000:
        return (False, "Your brain shutting down, you flop on the floor like a displaced fish.")
    elif num < 10000000000:
        return (False, "You very being weakens, you are now more mulch than badger.")
    else:
        return (True, "You can no longer handle the intense smells you are subjected to. With a last defiant grunt, you pass out.")

def pensley():
    print(
        "You find yourself in Pensley's shed-office. You groan, Pensley, the computer obsessed local boy. He is sitting at his desk, focussed entirely on his work. He suddenly looks up at you with a big smile on his face. He explains: 'Ah, you must be the volunteer I asked for. As you know, I have been busy teaching second-year C programming. I am trying to teach the complicated topic of recursion, which I really feel deserves a practical demonstration for the students to truly grasp the concept.'")
    print(
        "He continues: 'It is lucky I also have the assistance of Fiendish Hog as well. I think the two of you will do a tremendous job in demonstrating recursion. Ah, here he is now.'")
    action_one = input("Fiendish Hog casually trots in through the door, wearing a particularly wide grin. Pensley says 'We need to go now. The lecture is about to start'. Pensley and Hog leave the room. Type 'follow them' to follow.\n")
    if not validate_input(['follow them'], action_one):
        print("Fiendish Hog sees you and calls over, saying 'Hurry up! The lecture is about to start.'. You change your mind and decide to follow them, as you are concerned that refusal will affect your lab marks.")
    print(
        "You follow Pensely and Hog into PLT, where a group of second year students are patiently waiting. Pensley addresses the room: 'Now class, remember we discussed recursion in the previous lecture. Well, in order to really grasp the concept I feel it is best to watch a practical demonstration. Thankfully, we have two very kind volunteers who are willing to do just that.' The room bursts into applause as you walk up to the front with Fiendish Hog.")
    action_two = input(
        "Fiendish Hog turns to you and says 'It is time for the practical demonstration. Stand against the wall with you arms stretched out.' Type 'stretch arms' to assume the position.\n")
    while not validate_input(['stretch arms'], action_two):
        action_two = input("Fiendish Hog sighs and says: 'There really is no way out of this. Stretch your arms.' Type 'stretch arms' to assume the position.\n")
    print("Fiendish Hog addresses the room: 'I will demonstrate the factorial function, which is often implemented in a recursive manner'. Fiendish Hog walks over to a shopping trolley full of rotten fruit.")
    fac = random.randrange(-1, 21)
    if fac == -1:
        print(urethral_insertion(fac))
        print(urethral_sensation(fac)[1])
        print("GAME OVER")
        return
    else:
        count = 1
        for i in range(0, fac):
            count *= (i + 1)
            sensation = urethral_sensation(count)
            print(urethral_insertion(count) + " " + sensation[1])
            if sensation[0] == True:
                print("GAME OVER")
                return
            if i != fac - 1:
                action = input("Fiendish Hog says 'I'm not done yet!'. Type 'wait' to wait for Fiendish Hog to finish.\n")
                if not validate_input(['wait'], action):
                    print(f"You try to {action} but you find that you are unable to.")
    print("You breathe a sigh of relief as it appears that the demonstration is over. However, before you could leave, Fiendish Hog walks over to you and slams a rotten pumpkin over your head. After several hours of intense clawing you manage to make eye holes so you can see your way home. Once home you collapse on the floor, exhausted, pumpkined and ciderless.\nGAME OVER")
    print("GAME OVER")

def orchard():
    print("You find yourself in an orchard. Apple trees of every type, from the sourest of crab apples to the sweetest of Fuji, even a few pear trees thrown in to mix it up. You snuffle with delight at this bountiful hoard, gorging yourself and leaving with all you can carry.\n Congratulations, YOU WIN.")

def farmer_granger():
    print("He sees a clear trail from your den to where you stand, thus revealing your den's location. He"
    "takes the opportunity; sneaking to your den and stealing all your apples, must and cider.\n GAME OVER")


"""
Main console run
"""

woods_area = input("Which part of the woods do you want to visit? Type 'Rolling Hills' or 'Farmers House'.\n")
woods_area = woods_area.lower()

if woods_area == 'rolling hills':
    action_one = input(
        "You enter the rolling hills to find it eerily quiet. You hear an odd shuffling sound, as if papers were being turned over, coming from within one of the mounds. Type 'Enter' or 'Move on'.\n")
    action_one = action_one.lower()
    if action_one == "enter":
        print(
            "In the mound you find Mrs Scrumpy going over your tax returns\n'So there you are you no good work dodger! Been off cider hunting again  no doubt? Well you can forget about it until you've done these tax returns'.\nGAME OVER")
    elif action_one == "move on":
        action_two = input(
            "You take a left and shuffle through a hole into the largest hill. You enter a cross-roads of tunnels. There are multiple ways to go, each with its scent; you must pick one to follow. Type 'apple-scented tunnel', 'Pear scented-tunnel', 'cigar-scented tunnel', 'sweat-scented tunnel' or 'pencil-scented tunnel'.\n")
        action_two = action_two.lower()
        if action_two == 'apple-scented tunnel':
            orchard()
        elif action_two == 'pear-scented tunnel':
            print("You follow the sweet smell of pears, shuffling forward with a snuffle of anticipation. Suddenly you hear a snap behind you and you realise you're trapped. You hear an excited\n 'ooh aar!'\n Farmer Granger.")
            farmer_granger()
        elif action_two == 'cigar-scented tunnel':
            slyfox()
        elif action_two == 'sweat-scented tunnel':
            grumpy_bull()
        elif action_two == 'pencil-scented tunnel':
            pensley()
        else:
            did_not_enter("a tunnel")

    else:
        did_not_enter("an action")
elif woods_area == 'farmers house':
    print(
        "You leave the woods to the Farmer's House. Farmer Granger comes out of his cottage to see you trotting along.")
    farmer_granger()
else:
    did_not_enter("a part of the woods")
