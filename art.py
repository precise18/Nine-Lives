"""ASCII art and visual elements for the game"""

HANGMAN_STAGES = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,  # 0 lives - full hangman
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,  # 1 life
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,  # 2 lives
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |      
       -
    """,  # 3 lives
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |      
       -
    """,  # 4 lives
    """
       --------
       |      |
       |      O
       |      
       |      
       |      
       -
    """,  # 5 lives
    """
       --------
       |      |
       |      
       |      
       |      
       |      
       -
    """,  # 6 lives
    """
       --------
       |      
       |      
       |      
       |      
       |      
       -
    """,  # 7 lives
    """
       
       
       
       
       
       
       -
    """,  # 8 lives
    """
       
       
       
       
       
       
       
    """   # 9 lives - empty gallows
]

def get_hangman_art(lives_remaining, max_lives):
    """Get the appropriate hangman stage based on remaining lives"""
    stage_index = max(0, min(8, max_lives - lives_remaining))
    return HANGMAN_STAGES[stage_index]

def display_title():
    """Display simple pink welcome screen - always works"""
    PINK = '\033[95m'
    HOT_PINK = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    print(f"""
{HOT_PINK}============================================{RESET}
{HOT_PINK}                                          {RESET}
{HOT_PINK}   {PINK}🐱 {BOLD}WELCOME TO NINE LIVES{PINK} 🐱        {RESET}
{HOT_PINK}                                          {RESET}
{HOT_PINK}   A word guessing game with a twist      {RESET}
{HOT_PINK}                                          {RESET}
{HOT_PINK}   {PINK}❤️{RESET}  Lives: {BOLD}9{HOT_PINK}                         {RESET}
{HOT_PINK}   {PINK}💀{RESET}  Wrong letter: {BOLD}-1 life{HOT_PINK}              {RESET}
{HOT_PINK}   {PINK}⚠️{RESET}  Wrong word: {BOLD}-2 lives{HOT_PINK}              {RESET}
{HOT_PINK}   {PINK}💡{RESET}  Type {BOLD}'hint'{RESET} for a clue{HOT_PINK}             {RESET}
{HOT_PINK}                                          {RESET}
{HOT_PINK}   {PINK}🎀  Good luck and have fun!  🎀{HOT_PINK}      {RESET}
{HOT_PINK}                                          {RESET}
{HOT_PINK}============================================{RESET}
    """)