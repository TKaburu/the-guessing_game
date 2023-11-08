from get_word import get_word


def play_again():
    run_game = input("\nWould you like to play again? yes (y) or no (n) ").lower()
    
    if run_game == "yes" or run_game == "y":
        start_game()
    elif run_game == "no" or run_game == "n":
        pass
    else:
        print("Please enter a valid option: (y) for yes or (n) for no ")


def start_game():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = get_word()
    letters_guessed = []
    correct_guess = "-" * len(word)
    lives = 12

    print("The word contains", len(word), "letters")

    while True:
        if lives > 0:
            print("You have ", lives, "lives")
            users_guess = input("\nGuess the letter: ").lower()
            
            if users_guess in alphabet and len(users_guess) == 1:
                if users_guess in letters_guessed:
                    print("Sorry, the letter", users_guess, "has already been played")
                    lives = lives - 1
                elif users_guess in word:
                    print("Good job! Letter", users_guess, "is part of the word")
                    letters_guessed.append(users_guess)
                    correct_guess = "".join(letter if letter in letters_guessed else " - " for letter in word)
                else:
                    print("Sorry, the letter", users_guess, "is not part of the word")
                    letters_guessed.append(users_guess)
                    lives = lives - 1
            else:
                print("Please enter a valid letter")

            print("Current progress:", " ".join(correct_guess).upper())
            print("Letters guessed: ", " ".join(letters_guessed))

            if correct_guess == word:
                print("\nCongratulations! You've guessed ", word, "correct.")
                break
        else:
            print("\nGame over! The word was ", word)
            break
    play_again()
start_game()
