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
    """Display game title art"""
    print("""
╔═══════════════════════════════════════╗
║        🐱  NINE LIVES  🐱             ║
║                                       ║
║   A word guessing game where you      ║
║   have 9 lives to guess the secret    ║
║   word. Each wrong letter costs 1     ║
║   life. Wrong word costs 2 lives!     ║
║                                       ║
║   Type 'hint' for a helpful clue!     ║
║                                       ║
║   Can you save the cat? 🐱❤️          ║
╚═══════════════════════════════════════╝
    """)