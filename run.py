import colorama
from colorama import Fore
colorama.init(autoreset=True)

player_name = None
gameover_qs = f"""{Fore.BLUE}
A - TRY AGAIN
B - FINISH GAME
"""

print(f"{Fore.BLUE}T H E\nH A N G M A N")
print(f"""
E N T E R   Y O U R   N A M E   B E L O W
                  """)

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

def main():
    """
    The game begins with a word that has to be guessed.
    When the game climaxes, the player is given the choice to play again or exit game
    """
     # Let player put in own name to play hangman
    while True:
        player_name = input(f"\n{Fore.BLUE}NAME:\n>>> ").strip().upper()
        if len(player_name) < 3:
            print(f"{Fore.RED}This is not a valid name!")
            continue
        else:
            break
    print(f"""{Fore.MAGENTA}\n
    HELLO {player_name}, WELCOME TO THE HANGMAN GAME!\n""")
    
    input(f"""\n{Fore.BLUE}
    {player_name}, PRESS ENTER TO START THE GAME.\n\n\n    >>> """)

    play_game = True
    while True:
        if play_game:
            

        player_choice = input(f"{gameover_qs}>>> ").lower()
        if player_choice == "a":
            print(f"\nYour choice is to keep playing\n")
            play_game = True
        elif player_choice == "b":
            print(f"{Fore.RED}\nGame Finished...")
            print(f"""{Fore.BLUE}
            \nThanks for playing, {player_name.capitalize()}.
            \nHope to see you again soon!\n""")
            break
        else:
            print(f"""{Fore.MAGENTA}\n
            That is not a valid option. Please try again.\n""")
            play_game = False

if __name__ == '__main__':
    main()