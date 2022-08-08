import random

random.seed()

def orchard():
    print("You find yourself in an orchard. Apple trees of every type, from the sourest of crab apples to the sweetest of Fuji, even a few pear trees thrown in to mix it up. You snuffle with delight at this bountiful hoard, gorging yourself and leaving with all you can carry.\n Congratulations, YOU WIN.")

def slyfox():

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    play_or_not = input(f"You enter Sly Fox's den. You find him in an ebullient mood and he engages you in conversation. 'Good morning fine badger', he cheerfully says. On a day like this I just cannot help but admire the beauty of the countryside. Breathing in this fresh air, it makes me feel young and energetic again...'. You wonder where this setup will end and consider fleeing, but he continues; 'It makes me think of when I was a young fox and truly loved to play games. Shall we play a game noble badger? Rock, paper, scissors.' To play, type 'play'\n")
    play_or_not = play_or_not.lower()
    if play_or_not == 'play':
        try:

          user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
          isinstance(user_choice, int)
        except:
          print(f"Sly Fox's cheerful demeanor suddenly vanishes. He looks you dead in the eye and speaks; 'you typed {user_choice}. Not only is that not one of 0, 1 or 2, its not even an integer. You have lost harder than anyone else who has ever played this game. I could have entered this as an elif. I chose instead to throw an exception so that you have to read this unpleasant red text.'\nGAME OVER")

        images = [rock, paper, scissors]
        computer_choice = int(random.randint(0,2))
        if user_choice > 2 or user_choice < 0:
          print (f"Sly Fox looks annoyed. He speaks to you; 'You chose an invalid number. You lose. At everything.' He pulls a level at the side of his den; a hidden spring-powered platform launches you into the air and you land in a manure pile.\nGAME OVER")
        else:
          user_choices_image = images[user_choice]
          computer_choices_image = images[computer_choice]
          if computer_choice == user_choice:
            print (f"You chose {user_choices_image}.\nSly Fox chose {computer_choices_image}. Its a draw. Sly Fox reaches out to shake your hand, then grasps yours so tight you cannot escape. He begins the most elegant tale of fox history you have ever heard, encapsulating you. It continues, drifting you into a state of bewitched nirvana. You gladly say good bye to this life, having known a bliss that could never be bested.\nGAME OVER")
          elif computer_choice == 0 and user_choice == 2:
            print (f"You chose {user_choices_image}.\nSly Fox chose {computer_choices_image}; You lose. In a mocking of your poor choice sly fox pulls out a pair of scissors and in one deft motion snips your pocket watch from your waist coat before booting you out the door.\nGAME OVER.")
          elif computer_choice > user_choice:
            print (f"You chose {user_choices_image}.\nSly Fox chose {computer_choices_image}. You lose. Sly Fox smiles a wry smile.\n 'Never mind'\n he says.\n'Here's a consolation prize', he opens a door to his garden to reveal a pile of apples with one perfect looking cox apple atop. Entranced, you dive into the pile and discover that all the other apples are rotten to the core, beyond what even fermentation can save.\nGAME OVER")
          else:
            print (f"You chose {user_choices_image}.\nSly Fox chose {computer_choices_image}. You win. Sly Fox smiles softly and lifts his glasses to look at your unimparied. He lets out a gentle sigh and whispers 'I'm glad its you.' He pulls open a bookcase, removing it from the wall to reveal a secret passage. You enter and find yourself in the land of Fox history. Each wall is covered with the most intricate of tapestries, telling of foxes of the greatest heroism and the most dastardly of deeds. Or so it was, 678 years ago. Trapped in this realm of impossible geometry you wonder, will you ever feel Earth again? One day, you find a single tapestry askew. You move other to correct it and it slips to the floor, revealing a door way. You enter and following a growing light.\n")
            orchard()