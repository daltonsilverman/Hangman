import random


# Allows for file set-up and user-input
def main():
    # Creates dictionary that attaches possible user inputs to file paths for an easier user experience
    file_chooser = {
        "animals": "src/animals.txt",
        "cars": "src/cars.txt",
        "movies": "src/movies.txt",
        "music": "src/music.txt",
        "sports": "src/sports.txt"
    }
    mode = input("Would you like to use a custom word (enter custom) or have one selected (enter preselected): ") \
        .lower()  # Allows user to select whether they want to enter a custom word or have the game choose for them
    while mode != "custom" and mode != "preselected":  # Error-protection ensuring only valid inputs
        mode = input("Please enter 'preselected' or 'custom' into the console: ").lower().strip()
    if mode == "custom":
        word = input("Please enter a word: ").lower().strip()  # User chooses word for gameplay
        while word.isalpha() is False:
            word = input("Please enter a valid word: ") # Error protection to ensure word is alphabetical
        hangman_game(word)
    else:
        # Allows user to select what category they want their generated word from
        category = input("Please enter one of the follow categories: animals, cars, movies, music, sports ").lower()
        while (category != "animals" and category != "cars" and category != "movies" and category != "music" and
               category != "sports"):
            category = input("Please enter 'animals', 'cars', 'movies', 'music', or 'sports': ").lower()
        with open(file_chooser[category], 'r') as file:
            word_list = file.readlines()
        word = word_list[random.randint(0, len(word_list)+1)].lower().strip()  # Takes random word from .txt file
        hangman_game(word)


# Draws hangman using ASCII-art based on number of incorrect guesses
def draw_hangman(guess_num):
    if guess_num == 1:
        print("   _\n  |_|\n")
    elif guess_num == 2:
        print("   _\n  |_|\n   |\n")
    elif guess_num == 3:
        print("   _\n  |_|\n --|\n")
    elif guess_num == 4:
        print("   _\n  |_|\n --|--\n")
    elif guess_num == 5:
        print("   _\n  |_|\n --|--\n  /\n")
    elif guess_num == 6:
        print("   _\n  |_|\n --|--\n  / \\ \n GAME OVER \n")


def hangman_game(word):
    winner = False
    incorrect_guesses = 0
    guesses = 0
    incorrect_letters = set()
    correct_letters = set()
    word_display = []
    for i in range(len(word)):
        word_display.append("_")  # Creates blank spaces in word display for user to see
    while incorrect_guesses < 6: # Allows user to input a guess as long as limit has not been exceeded
        guess = input("Please enter a letter: ")
        while len(guess) != 1 and (guess.isalpha() is False or guess in incorrect_letters or guess in correct_letters):
            if guess.isalpha() is False:
                print("Error: Not a valid letter")
                guess = input("Please enter a letter a-z")  # Ensures guess is alphabetical and only a singular letter
            if guess in incorrect_letters or guess in correct_letters:
                print("Error: That letter has already been used")
                guess = input("Please enter a letter that has not been used")  # Ensures letter hasn't been guessed
        guesses += 1
        guess = guess.lower()
        if guess in word:
            correct_letters.add(guess)  # Keeps track of correct letters
            for i in range(len(word)):  # Replaces blanks with letter guesse
                if word[i] == guess:
                    word_display[i] = guess
        else:
            incorrect_letters.add(guess)
            incorrect_guesses += 1
        # Displays statistics to user about progress in game
        print(f"\n Correct Letters: {correct_letters}\n")
        print(f"\n Incorrect Letters: {incorrect_letters}\n")
        print(f"\n Moves: {guesses}\n")
        print(f"Progress: {word_display}")
        draw_hangman(incorrect_guesses)

        if "_" not in word_display:  # Detects victory
            print(f"\n CONGRATULATIONS WINNER!!!!! \n You guessed the word in {guesses} moves. Can you do better?\n")
            winner = True
            break
    if winner is False:  # Detects loss
        print("\nYou lost :(. Try again?\n")


if __name__ == "__main__":
    main()
