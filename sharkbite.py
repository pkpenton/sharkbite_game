import random
import shark_pics

movie_titles_easy = [
    "titanic",
    "cinderella",
    "inception",
    "frozen",
    "vertigo",
    "watchmen",
    "gladiator",
    "transformers",
    "goodfellas",
    "scarface",
    "twilight",
    "frankenstein",
    "ratatouille",
    "rocky",
    "skyfall",
]

class colors:
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    WHITE = '\033[37m'

secret_word = random.choice(movie_titles_easy)
correct_letters = ""
incorrect_letters = ""
game_over = False

def display_game(SHARK_PICS, correct_letters, incorrect_letters, secret_word):
    print colors.BLUE + shark_pics.SHARK_PICS[len(incorrect_letters)]

    if len(incorrect_letters) != 0:
        print "Incorrect guesses: "
        for letter in incorrect_letters:
            print letter,

    disguised_word = len(secret_word) * "_"

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            disguised_word = disguised_word[:i] + secret_word[i] + disguised_word[i+1:]

    print colors.GREEN + "\nYour word is %s letters long.\n" % len(secret_word) + disguised_word


def letter_guess(already_guessed):
    while True:
        letter_guess = raw_input("Please guess a letter: ").lower()
        if len(letter_guess) > 1:
            print "Please enter a single letter."
        elif letter_guess not in 'abcdefghijklmnopqrstuvwxyz':
            print "Please enter a letter."
        elif letter_guess in already_guessed:
            print "You already guessed that letter. Try again."
        else:
            return letter_guess


name = raw_input("\nWelcome to SHARKBITE! What's your name? ")
print colors.GREEN + """\nHi, %s! Let's begin...\n
This little fish is in trouble!\n
You must guess the secret word one letter at a time in order to save the fish from the shark!\n
The theme of your secret word is: Movie Titles.
""" % (name)

while True:
    display_game(shark_pics.SHARK_PICS, correct_letters, incorrect_letters, secret_word)
    guesses = letter_guess(correct_letters + incorrect_letters) 

    if guesses in secret_word:
        correct_letters += guesses

        guessed_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                guessed_all_letters = False
                break
        if guessed_all_letters:
            print colors.CYAN + """
            Good job! You guessed the secret word: '%s'\n
                And you saved the fish from the shark!

                      O                            
                     o   Thank you!          
                                 
                     o  _,`._  _  
                      ,O     \/ |
                      )  ((( , < 
                        `-\,-'`-'
            """ % secret_word.capitalize()
            game_over = True
    else:
        incorrect_letters += guesses

        if len(incorrect_letters) == (len(shark_pics.SHARK_PICS)-1):
            display_game(shark_pics.SHARK_PICS, correct_letters, incorrect_letters, secret_word)
            print colors.RED + """
            Uh-oh! You ran out of guesses!\n
            The secret word was: %s

                 _________         .    .
                (..       \_    ,  |\  /|
                 \       0  \  /|  \ \/ /
                  \______    \/ |   \  /
                     vvvv\    \ |   /  |
              YUM!   \^^^^  ==   \_/   |
                      `\_   ===    \.  |
                      / /\_   \ /      |
                      |/   \_  \|      /
                             \________/ 
            """ % secret_word.capitalize()
            game_over = True

    if game_over:
        play_again = raw_input(colors.MAGENTA + "Would you like to play again? (yes/no) ").lower()
        if play_again == "yes":
            correct_letters = ""
            incorrect_letters = ""
            game_over = False
            secret_word = random.choice(movie_titles_easy)
        else:
            print colors.WHITE + "Thanks for playing!"
            exit()
