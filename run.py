"""
Main file
"""
import os
import random
import gspread
import colorama
from google.oauth2.service_account import Credentials
from colorama import Fore
from tabulate import tabulate
from hangman_structure import game_details, phases

colorama.init(autoreset=True)

# List of words for the game
words = [
    "Serendipity",
    "Mellifluous",
    "Quixotic",
    "Zephyr",
    "Enigmatic",
    "Nebulous",
    "Ephemeral",
    "Pernicious",
    "Halcyon",
    "Obfuscate",
    "Quagmire",
    "Labyrinthine",
    "Plenitude",
    "Euphoria"
]

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Try to connect to Googlesheets, if error notify user

try:
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('hangman-pp3')
    LEADERBOARD_WORKSHEET = SHEET.worksheet("leaderboard")

except FileNotFoundError:
    print("Error: please refresh the browser\n")


# Initialize constant
CORRECT_CHOSEN = 5 # Score awarded for each correct letter

gameover_qs = f"""{Fore.GREEN}
A - TRY AGAIN
B - FINISH GAME
C - VIEW LEADERBOARD
"""

# Introduction and player name input
print(f"{Fore.YELLOW}T H E\nH A N G M A N")
print("""
E N T E R   Y O U R   N A M E   B E L O W
                  """)


# Function to clear the terminal screen
def clear_terminal():
    """
    function to clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Main game function
def game(word_to_guess, player_name):
    """
    Main game function
    """
    complete_word = "_" * len(word_to_guess)
    chosen = False
    chosen_letters = []
    incorrect_picks = []
    correct_picks = 0
    tries = 7
    score = 0

    print(f"""{Fore.MAGENTA}
    YOUR WORD HAS {len(word_to_guess)} LETTERS""")
    print(display_gallows(tries)) # Display the initial state of the hangman
    word_progress(f"{complete_word}")

    while not chosen and tries > 1:
        print(f"{Fore.MAGENTA}\nINCORRECT PICKS:\n{incorrect_picks}\n")
        show_score(score)
        if tries > 1:
            print(f"{Fore.GREEN}YOU HAVE {tries} TRIES")
        else:
            print(f"{Fore.RED}YOU HAVE {tries} GOES LEFT\n")
        letter_input = input(f"{Fore.BLUE} CHOOSE A LETTER AND HIT ENTER:\n ").upper()
        clear_terminal()


        # Check if the player has already chosen the letter
        if len(letter_input) == 1 and letter_input.isalpha():
            if letter_input in chosen_letters:
                print(f"""{Fore.MAGENTA}\n
                YOU ALREADY ENTERED {letter_input}\n""")
            # Check if the letter chosen is not in the word
            elif letter_input not in word_to_guess:
                print(f"{Fore.CYAN} HARD LUCK {letter_input} IS NOT IN THE WORD")
                tries -= 1
                chosen_letters.append(letter_input)
                incorrect_picks.append(letter_input)
            # Check if the letter chosen is not in the word
            else:
                print(f"{Fore.YELLOW} WELL DONE {letter_input} IS IN THE WORD")
                chosen_letters.append(letter_input)
                correct_picks += 1
                word_as_list = list(complete_word)
                indexes = [i for i, letter in enumerate(
                          word_to_guess) if letter == letter_input]
                for index in indexes:
                    word_as_list[index] = letter_input
                complete_word = "".join(word_as_list)
                if "_" not in complete_word:
                    chosen = True
                    print(f"""{Fore.BLUE}\n
                        GREAT, THE WORD WAS {complete_word}, YOU GOT IT!\n""")
                    score += 30
                score += CORRECT_CHOSEN * len(indexes)
        else:
            print(f"{Fore.MAGENTA}\nENTRY NOT VALID.\n")
        print(display_gallows(tries))
        word_progress(f"{complete_word}")

    outcome(chosen, word_to_guess, score, player_name)

# Function to display the final outcome of the game
def outcome(chosen, word_to_guess, score, player_name):
    """
    Verify if the player completes game
    """
    if not chosen:
        print(F"""{Fore.RED}
        HARD LUCK {player_name}, THE CORRECT WORD WAS {word_to_guess}!
        """)
    LEADERBOARD_WORKSHEET.append_row([player_name, int(score)])
    show_score(score)

# Function to display the current progress in word guessing
def word_progress(complete_word):
    """
    Prints correct guesses
    """
    for i in complete_word:
        print(i, end=" ")

# Function to display the hangman based on the number of tries left
def display_gallows(tries):
    """
    Show the Hangman phases at the beginning of the game 
    and update them whenever the player makes an incorrect letter choice.
    """
    return phases[tries]

# Function to show the player's current score
def show_score(score):
    """
    Show score throughout the game
    """
    print(f"SCORE: {score}")


# Main game loop
def main():
    """
    The game begins with a word that has to be guessed.
    When the game climaxes, the player is given the choice to play again or exit game
    """
    # Let player put in own name to play hangman
    while True:
        player_name = input(f"{Fore.BLUE}NAME:  ").strip().upper()
        if len(player_name) < 3:
            print(f"{Fore.RED}This is not a valid name,\n"
                            "please enter at least 3 letters!")
            continue
        break
    print(f"""{Fore.MAGENTA}
    HELLO {player_name}, WELCOME TO THE HANGMAN GAME!""")
    print(f"{Fore.BLUE}{game_details[0]}")
    input(f"""{Fore.BLUE}
    {player_name}, PRESS ENTER TO START THE GAME """)
    clear_terminal()
    play_game = True

    while True:
        if play_game:
            word_to_guess = get_word()
            game(word_to_guess, player_name)

        player_choice = input(f"{gameover_qs} ").lower()
        if player_choice == "a":
            print("\nYour choice is to keep playing\n ")
            play_game = True
        elif player_choice == "b":
            print(f"{Fore.RED}Game Finished...")
            print(f"""{Fore.BLUE}
            Thanks for playing, {player_name.capitalize()}.
            \nHope to see you again soon!\n""")
            break

        elif player_choice == "c":
            # Create a list to store the all values in the leaderboard
            data_list = LEADERBOARD_WORKSHEET.get_all_values()
            # Sort rows based on the score which is index 1 on each row
            sorted_list = sorted(data_list, key=lambda x: x[1], reverse=True)
            clear_terminal()
            print(tabulate(sorted_list[:10], ["Name", "Score"], tablefmt="fancy_outline"))
            play_game = False
        else:
            print(f"""{Fore.MAGENTA}\n
            That is not a valid option. Please try again.\n""")
            play_game = False

# Function to get a word to guess from the list of words
def get_word():
    """
    Get a word to guess from the list of words
    """
    word_to_guess = random.choice(words)
    return word_to_guess.upper()

# Start the game if the script is run as the main program
if __name__ == '__main__':
    main()
