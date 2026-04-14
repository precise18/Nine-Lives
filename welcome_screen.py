"""Welcome screen designs and visual elements"""

# ANSI color codes for terminal colors
class Colors:
    """Color definitions for terminal output"""
    PINK = '\033[95m'
    HOT_PINK = '\033[38;5;205m'
    LIGHT_PINK = '\033[38;5;218m'
    DARK_PINK = '\033[38;5;161m'
    DEEP_PINK = '\033[38;5;162m'
    ROSE = '\033[38;5;174m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def show_welcome():
    """Display simple but elegant pink welcome screen"""
    c = Colors()
    
    print(f"""
{c.HOT_PINK}╔══════════════════════════════════════════════════════════╗
║                                                                  ║
║                    {c.BOLD}{c.PINK}🐱 NINE LIVES 🐱{c.HOT_PINK}                      ║
║                                                                  ║
║                    {c.LIGHT_PINK}A Word Guessing Game{c.HOT_PINK}                     ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                                  ║
║     {c.ROSE}❤️{c.HOT_PINK}  {c.BOLD}You have 9 lives{c.RESET}{c.HOT_PINK} to guess the secret word{c.HOT_PINK}        ║
║                                                                  ║
║     {c.ROSE}💀{c.HOT_PINK}  Each wrong letter costs {c.BOLD}1 life{c.RESET}{c.HOT_PINK}                     ║
║                                                                  ║
║     {c.ROSE}⚠️{c.HOT_PINK}  Each wrong word guess costs {c.BOLD}2 lives{c.RESET}{c.HOT_PINK}                ║
║                                                                  ║
║     {c.ROSE}💡{c.HOT_PINK}  Type {c.BOLD}'hint'{c.RESET}{c.HOT_PINK} for a helpful clue{c.HOT_PINK}                ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                                  ║
║              {c.BOLD}{c.PINK}Can you save the cat?{c.HOT_PINK} 🐱                    ║
║                                                                  ║
║              {c.LIGHT_PINK}Good luck and have fun!{c.HOT_PINK} 🎀                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════╝{c.RESET}
    """)