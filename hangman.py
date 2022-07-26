#Step 5

def game_of_hangman():

    import random
    from hangman_word_list import word_list
    from hangman_art import stages, logo

    game_result = 'lose' # set to lose unless victory achieved.
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6
    print(logo)

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    guess_list = [] #A list to append user guesses to.
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in guess_list:
            print(f"You have already guessed {guess}. Please guess another letter.")
            guess = input("Guess a letter: ").lower()
        else:
            guess_list += guess #add the user guess to the list of guesses.
            #Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    print(f"Your guess, {guess}, is in the word.")
                    display[position] = letter

            #Check if user is wrong.
            if guess not in chosen_word:
                print(f"Your guess, {guess}, is not in the word.")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose.")

            #Join all the elements in the list and turn it into a String.
            print(f"{' '.join(display)}")

            #Check if user has got all letters.
            if "_" not in display:
                end_of_game = True
                game_result = 'win'
                print("You win.")

            print(stages[lives])

    return game_result