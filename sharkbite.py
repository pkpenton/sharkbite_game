import random
import shark_pics

us_states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]

state_capitals = [
    'Albany',
    'Annapolis',
    'Atlanta',
    'Augusta',
    'Austin',
    'Baton Rouge',
    'Bismarck',
    'Boise',
    'Boston',
    'Carson City',
    'Charleston',
    'Cheyenne',
    'Columbia',
    'Columbus',
    'Concord',
    'Denver',
    'Des Moines',
    'Dover',
    'Frankfort',
    'Harrisburg',
    'Hartford',
    'Helena',
    'Honolulu',
    'Indianapolis',
    'Jackson'
    'Jefferson City'
    'Juneau',
    'Lansing',
    'Lincoln',
    'Little Rock'
    'Madison',
    'Montgomery',
    'Montpelier',
    'Nashville',
    'Oklahoma City',
    'Olympia',
    'Phoenix',
    'Pierre',
    'Providence',
    'Raleigh',
    'Richmond',
    'Sacramento',
    'Saint Paul',
    'Salem',
    'Salt Lake City',
    'Santa Fe',
    'Springfield',
    'Tallahassee',
    'Topeka',
    'Trenton',
]

us_presidents = [
    "George Washington",
    "John Adams",
    "Thomas Jefferson",
    "James Madison",
    "James Monroe",
    "John Quincy Adams",
    "Andrew Jackson",
    "Martin Van Buren",
    "William H Harrison",
    "John Tyler",
    "James K Polk",
    "Zachary Taylor",
    "Millard Fillmore",
    "Franklin Pierce",
    "James Buchanan",
    "Abraham Lincoln",
    "Andrew Johnson",
    "Ulysses S Grant",
    "Rutherford B Hayes",
    "James A Garfield",
    "Chester A Arthur",
    "Grover Cleveland",
    "Benjamin Harrison",
    "Grover Cleveland",
    "William McKinley",
    "Theodore Roosevelt",
    "William H Taft",
    "Woodrow Wilson",
    "Warren G Harding",
    "Calvin Coolidge",
    "Herbert Hoover",
    "Franklin D Roosevelt",
    "Harry S Truman",
    "Dwight D Eisenhower",
    "John F Kennedy",
    "Lyndon B Johnson",
    "Richard M Nixon",
    "Gerald R Ford",
    "Jimmy Carter",
    "Ronald Reagan",
    "George H W Bush",
    "Bill Clinton",
    "George W Bush",
    "Barack Obama",
]

class Colors:
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    WHITE = '\033[37m'


name = raw_input("\nWelcome to SHARKBITE! What's your name? ")
print Colors.GREEN
print """\nHi, %s! Let's begin...\n
This little fish is in trouble and needs your help!\n
                      O                            
                     o   Help!          
                                 
                     o  _,`._  _  
                      ,O     \/ |
                      )  ((( , < 
                        `-\,-'`-' \n
You must guess a secret word one letter at a time in order to save the fish from the shark!
""" % (name)


def theme_choice():
    secret_word = None
    while secret_word is None:
        theme = raw_input("""Please pick a theme for your secret word:\n
            1 - US States
            2 - State Capitals
            3 - US Presidents\n""")
        if theme == "1":
            secret_word = random.choice(us_states).lower()
        elif theme == "2":
            secret_word = random.choice(state_capitals).lower()
        elif theme == "3":
            secret_word = random.choice(us_presidents).lower()
        else:
            print "Please enter only a single number."
    return secret_word

secret_word = theme_choice()


def display_game(SHARK_PICS, correct_letters, incorrect_letters, secret_word):
    print Colors.BLUE + shark_pics.SHARK_PICS[len(incorrect_letters)]

    if len(incorrect_letters) != 0:
        print Colors.RED + "Incorrect guesses: "
        for letter in incorrect_letters:
            print letter,

    disguised_word_list = []

    for letter in secret_word:
        if letter in correct_letters:
            disguised_word_list.append(letter)
        else:
            disguised_word_list.append('_')

    disguised_word = ''.join(disguised_word_list)

    # Another way to do this:

    # disguised_word = len(secret_word) * "_"

    # for i in range(len(secret_word)):
    #     if secret_word[i] in correct_letters:
    #         disguised_word[i] = secret_word[i]
    #         #disguised_word = disguised_word[:i] + secret_word[i] + disguised_word[i+1:]


    # List comprehension is fun! (yet aother way to do this):

    # disguised_word = ''.join([c if c in correct_letters else '_' for c in secret_word])

    print Colors.GREEN
    print "\nYour word is %s letters long." % len(secret_word)
    print disguised_word


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

correct_letters = " "
incorrect_letters = ""
game_over = False

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
            print Colors.CYAN
            print """
            Good job! You guessed the secret word: '%s'\n
                And you saved the fish from the shark!

                      O                            
                     o   Thank you!          
                                 
                     o  _,`._  _  
                      ,O     \/ |
                      )  ((( , < 
                        `-\,-'`-'
            """ % secret_word.title()
            game_over = True
    else:
        incorrect_letters += guesses

        if len(incorrect_letters) == (len(shark_pics.SHARK_PICS)-1):
            display_game(shark_pics.SHARK_PICS, correct_letters, incorrect_letters, secret_word)
            print Colors.RED
            print """
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
            """ % secret_word.title()
            game_over = True


    if game_over:
        while game_over == True:
            play_again = raw_input(Colors.MAGENTA + "Would you like to play again? (yes/no) ").lower()
            if play_again in ['yes', 'y']:
            # if play_again == 'yes' or 'y':
                correct_letters = " "
                incorrect_letters = ""
                game_over = False
                secret_word = theme_choice()
            elif play_again in ['no', 'n']:
                print Colors.WHITE + "Thanks for playing!"
                exit()
            else:
                print "Please enter yes or no."
