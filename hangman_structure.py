"""
Hangman Structure file
"""
import colorama
from colorama import Fore
colorama.init(autoreset=True)

phases = [
 """
 """,
 # hangman 6
 Fore.RED +
 """                
                   ___________________
                   |                  |
                   |                 _|_
                   |                (o o)
                   |                 (~)
                   |               __/|\\__
                   |                  |
                   |                  |
                   |                 / \\
                   |               _/   \\_
                   |
                 __|__                              
 """,
 # hangman 5
 Fore.RED +
 """                 
                   ___________________
                   |                  |
                   |                 _|_
                   |                (o o)
                   |                 (~)
                   |               __/|\\__
                   |                  |
                   |                  |
                   |                ./ 
                   |               _/   
                   |
                 __|__                              
 """,
 #  hangman 4
 Fore.RED +
"""                
                   ___________________
                   |                  |
                   |                 _|_
                   |                (o o)
                   |                 (~)
                   |               __/|\\__
                   |                  |
                   |                  |
                   |                 
                   |                 
                   |
                 __|__                               
 """,
 # hangman 3
 Fore.RED +
 """                 
                   ___________________
                   |                  |
                   |                 _|_
                   |                (o o)
                   |                 (~)
                   |               __/|
                   |                  |
                   |                  |
                   |                 
                   |                  
                   |
                 __|__                             
 """,
 # hangman 2
 Fore.RED +
 """                
                   ___________________
                   |                  |
                   |                 _|_
                   |                (o o)
                   |                 (~)
                   |                  |
                   |                  |
                   |                  |
                   |                 
                   |                 
                   |
                 __|__                              
 """,
 # hangman 1
 Fore.RED +
 """                
                   ___________________
                   |                  |
                   |                 _|_
                   |                (o o)
                   |                 (~)
                   |               
                   |                  
                   |                  
                   |                 
                   |                  
                   |
                 __|__                              
 """,
 # hangman 0
 Fore.RED +
 """
         
                   ___________________
                   |                  |
                   |                  |
                   |                
                   |                 
                   |               
                   |                  
                   |                  
                   |                 
                   |                  
                   |
                 __|__                           
 """,
]

game_details = [
 # rules

"""
   H A N G M A N H A N G M         R U L E S           A N H A N G M A N H A H
   A                                                                         A
   N                                                                         N
   G          1.  Hangman is an objective based family game where a          G
   M              word is to be guessed using only letters.                  M
   A          2.  You will have several attempts but can only have 6         A
   N              incorrect guesses.                                         N
   H          3.  With each incorrect guess the hangmans body will           H
   A              populate.                                                  A
   N          4.  When the hangmans head and full body appear you lose.      N
   G          5.  For each correct letter the player receives 10pts.         G
   M                                                                         M
   A                                                                         A
   N H A N G M A N H A N G M A N H A N G M A N H A N G M A N H A N G M A N A N
"""
]
