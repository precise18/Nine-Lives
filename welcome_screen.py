def show_welcome():
    """Display simple but elegant pink welcome screen with decorative borders"""
    c = Colors()
    
    print(f"""
{c.HOT_PINK}╭──────────────────────────────────────────────────────────────────╮
│                                                                  │
│                     {c.BOLD}{c.PINK}🐱  NINE LIVES  🐱{c.HOT_PINK}                      │
│                                                                  │
│                  {c.LIGHT_PINK}✨ A Word Guessing Game ✨{c.HOT_PINK}                  │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│      {c.ROSE}❤️{c.HOT_PINK}     You have {c.BOLD}{c.PINK}9 LIVES{c.RESET}{c.HOT_PINK} to guess the secret word{c.HOT_PINK}                │
│                                                                  │
│      {c.ROSE}💀{c.HOT_PINK}     Each wrong letter costs {c.BOLD}{c.PINK}1 LIFE{c.RESET}{c.HOT_PINK}                    │
│                                                                  │
│      {c.ROSE}⚠️{c.HOT_PINK}     Each wrong word costs {c.BOLD}{c.PINK}2 LIVES{c.RESET}{c.HOT_PINK}                   │
│                                                                  │
│      {c.ROSE}💡{c.HOT_PINK}     Type {c.BOLD}{c.PINK}'hint'{c.RESET}{c.HOT_PINK} for a magical clue{c.HOT_PINK}                  │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│              {c.BOLD}{c.PINK}🐱  Can YOU save the cat?  🐱{c.HOT_PINK}                  │
│                                                                  │
│                  {c.LIGHT_PINK}🎀  Good luck!  🎀{c.HOT_PINK}                          │
│                                                                  │
│              {c.LIGHT_PINK}══════════════════════════════{c.HOT_PINK}                      │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯{c.RESET}
    """)