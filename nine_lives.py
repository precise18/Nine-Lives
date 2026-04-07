import random
import sys

class NineLives:
    def __init__(self):
        self.word_list = [
            # Animals
            "CAT", "DOG", "COW", "PIG", "DUCK", "FISH", "BIRD", "FROG",
            "LION", "BEAR", "TIGER", "ZEBRA", "MONKEY", "RABBIT", "MOUSE",
            "EAGLE", "SHARK", "WHALE", "SNAKE", "DEER",
            
            # Colors
            "RED", "BLUE", "GREEN", "YELLOW", "BLACK", "WHITE", "PINK",
            "PURPLE", "ORANGE", "BROWN", "GRAY",
            
            # Food
            "CAKE", "MILK", "BREAD", "RICE", "SOUP", "EGGS", "MEAT",
            "APPLE", "MANGO", "GRAPE", "LEMON", "HONEY", "PIZZA", "BURGER",
            
            # Nature
            "SUN", "MOON", "STAR", "SKY", "CLOUD", "RAIN", "SNOW",
            "WIND", "TREE", "FLOWER", "GRASS", "LEAF", "ROCK", "OCEAN",
            
            # Home
            "BED", "CUP", "PEN", "BOOK", "BALL", "TOY", "HAT", "SHOE",
            "DOOR", "WINDOW", "TABLE", "CHAIR", "LAMP", "CLOCK",
            
            # Actions
            "RUN", "JUMP", "SING", "DANCE", "READ", "WRITE", "EAT", "SLEEP",
            "LAUGH", "CRY", "SMILE", "PLAY", "WORK", "STUDY"
        ]
        self.secret_word = ""
        self.hidden_word = []
        self.lives = 9
        self.guessed_letters = set()
        self.max_lives = 9
        
    def choose_word(self):
        """Randomly select a word from the word list"""
        self.secret_word = random.choice(self.word_list)
        self.hidden_word = ['_' for _ in self.secret_word]
        
    def give_hint(self):
        """Give a helpful hint about the word"""
        hints = {
            # Animals
            "CAT": "🐱 This animal says 'meow' and loves milk",
            "DOG": "🐕 This animal says 'woof' and is called man's best friend",
            "COW": "🐄 This animal gives us milk",
            "PIG": "🐷 This animal says 'oink' and loves mud",
            "DUCK": "🦆 This bird says 'quack' and loves water",
            "FISH": "🐟 This animal lives in water and has fins",
            "BIRD": "🐦 This animal has wings and can fly",
            "FROG": "🐸 This green animal jumps and says 'ribbit'",
            "LION": "🦁 The king of the jungle",
            "BEAR": "🐻 A large furry animal that loves honey",
            "TIGER": "🐯 A big cat with orange and black stripes",
            "ZEBRA": "🦓 An animal with black and white stripes",
            "MONKEY": "🐒 An animal that loves bananas and swings on trees",
            "RABBIT": "🐰 An animal with long ears that loves carrots",
            "MOUSE": "🐭 A small animal that loves cheese",
            
            # Colors
            "RED": "🔴 The color of apples and fire trucks",
            "BLUE": "🔵 The color of the sky and ocean",
            "GREEN": "🟢 The color of grass and leaves",
            "YELLOW": "🟡 The color of the sun and bananas",
            "BLACK": "⚫ The darkest color",
            "WHITE": "⚪ The color of snow and milk",
            "PINK": "🎀 The color of cotton candy",
            "PURPLE": "🟣 The color of grapes",
            "ORANGE": "🟠 The color of oranges and pumpkins",
            
            # Food
            "CAKE": "🎂 A sweet dessert often eaten at birthdays",
            "MILK": "🥛 A white drink from cows",
            "BREAD": "🍞 A food made from flour, often used for sandwiches",
            "RICE": "🍚 A grain that is a staple food in many countries",
            "SOUP": "🥣 A liquid food made from vegetables or meat",
            "EGGS": "🥚 Food that comes from chickens",
            "APPLE": "🍎 A round fruit that is red or green",
            "MANGO": "🥭 A sweet tropical fruit",
            "PIZZA": "🍕 Italian dish with cheese and toppings",
            "BURGER": "🍔 A sandwich with a patty",
            
            # Nature
            "SUN": "☀️ The star that gives us light and heat",
            "MOON": "🌙 The object that glows at night",
            "STAR": "⭐ A bright point of light in the night sky",
            "RAIN": "🌧️ Water falling from clouds",
            "SNOW": "❄️ White frozen water that falls in winter",
            "TREE": "🌳 A tall plant with a trunk and branches",
            "FLOWER": "🌺 A colorful plant part that blooms",
            "OCEAN": "🌊 A large body of salt water",
            
            # Home
            "BOOK": "📖 Something you read with pages",
            "PEN": "🖊️ A tool used for writing",
            "BED": "🛏️ Where you sleep",
            "CHAIR": "🪑 Where you sit",
            "LAMP": "💡 A device that gives light",
            "CLOCK": "⏰ A device that tells time"
        }
        
        if self.secret_word in hints:
            print(f"\n💡 HINT: {hints[self.secret_word]}")
        else:
            # Generic hint - show word length and first letter
            print(f"\n💡 HINT: The word has {len(self.secret_word)} letters")
            print(f"💡 HINT: First letter is '{self.secret_word[0]}'")
        
    def display_game_state(self):
        """Display current game state"""
        print("\n" + "="*50)
        print(f"❤️  LIVES: {'❤️ ' * self.lives}".rjust(30))
        print("="*50)
        print(f"\n📝 WORD: {' '.join(self.hidden_word)}")
        print(f"🎯 GUESSED LETTERS: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
        print(f"💀 LIVES REMAINING: {self.lives}/{self.max_lives}")
        
    def get_player_guess(self):
        """Get and validate player's guess"""
        while True:
            guess = input("\n🔤 Enter a letter, word, or 'hint': ").upper().strip()
            
            if not guess:
                print("❌ Please enter something!")
                continue
                
            if guess == "HINT":
                return guess, "hint"
                
            if not guess.isalpha():
                print("❌ Please enter only letters!")
                continue
                
            if len(guess) == 1:
                if guess in self.guessed_letters:
                    print(f"⚠️  You already guessed '{guess}'. Try a different letter!")
                    continue
                return guess, "letter"
            else:
                return guess, "word"
    
    def process_letter_guess(self, letter):
        """Process a single letter guess"""
        self.guessed_letters.add(letter)
        
        if letter in self.secret_word:
            # Correct guess - reveal letters
            count = 0
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.hidden_word[i] = letter
                    count += 1
            print(f"✅ Good guess! '{letter}' appears {count} time(s) in the word!")
            return True
        else:
            # Wrong guess - lose a life
            self.lives -= 1
            print(f"❌ Sorry! '{letter}' is not in the word. You lose a life!")
            return False
    
    def process_word_guess(self, word):
        """Process a full word guess"""
        if word == self.secret_word:
            # Correct word guess - reveal entire word
            self.hidden_word = list(self.secret_word)
            return True
        else:
            # Wrong word guess - lose 2 lives (big penalty)
            self.lives -= 2
            print(f"❌❌ Wrong word! '{word}' is not the secret word. You lose 2 lives!")
            return False
    
    def check_win(self):
        """Check if player has won"""
        return '_' not in self.hidden_word
    
    def check_loss(self):
        """Check if player has lost"""
        return self.lives <= 0
    
    def display_hangman(self):
        """Display hangman ASCII art based on lives remaining"""
        hangman_stages = [
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
        
        # Show appropriate hangman stage (reverse order - more lives = less hangman)
        stage_index = max(0, min(8, 9 - self.lives))
        print(hangman_stages[stage_index])
    
    def play(self):
        """Main game loop"""
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
        
        self.choose_word()
        
        while True:
            self.display_game_state()
            self.display_hangman()
            
            guess, guess_type = self.get_player_guess()
            
            if guess_type == "hint":
                self.give_hint()
                continue
            elif guess_type == "letter":
                self.process_letter_guess(guess)
            else:  # word guess
                if self.process_word_guess(guess):
                    print(f"\n🎉 AMAZING! '{guess}' IS THE WORD! 🎉")
                    self.hidden_word = list(self.secret_word)
                    self.display_game_state()
                    print(f"\n🌟 CONGRATULATIONS! YOU SAVED THE CAT! 🌟")
                    print(f"🏆 You guessed the word '{self.secret_word}' with {self.lives} lives remaining! 🏆")
                    self.play_again()
                    return
            
            if self.check_win():
                self.display_game_state()
                print(f"\n🌟 CONGRATULATIONS! YOU SAVED THE CAT! 🌟")
                print(f"🏆 You guessed the word '{self.secret_word}' with {self.lives} lives remaining! 🏆")
                self.play_again()
                return
                
            if self.check_loss():
                self.display_hangman()
                print(f"\n💀 GAME OVER! 💀")
                print(f"😭 The cat ran out of lives... The word was '{self.secret_word}'")
                self.play_again()
                return
    
    def play_again(self):
        """Ask player if they want to play again"""
        while True:
            choice = input("\n🐱 Play again? (yes/no): ").lower().strip()
            if choice in ['yes', 'y']:
                self.reset_game()
                self.play()
                return
            elif choice in ['no', 'n']:
                print("\n🐱 Thanks for playing! Meow! 🐱")
                sys.exit()
            else:
                print("Please enter 'yes' or 'no'")
    
    def reset_game(self):
        """Reset game state for new round"""
        self.lives = 9
        self.guessed_letters = set()
        self.choose_word()


class NineLivesEasyMode(NineLives):
    """Easy mode - 12 lives with super easy words"""
    def __init__(self):
        super().__init__()
        self.word_list = [
            # 3-letter easy words
            "CAT", "DOG", "COW", "PIG", "SUN", "MOON", "STAR", "CAR", "BUS",
            "RED", "BLUE", "HAT", "CUP", "BED", "PEN", "BOOK", "TOY", "BALL",
            
            # 4-letter easy words
            "FISH", "BIRD", "FROG", "DUCK", "LION", "BEAR", "CAKE", "MILK",
            "BREAD", "RICE", "SOUP", "EGGS", "TREE", "FLOWER", "GRASS",
            
            # 5-letter easy words
            "HAPPY", "SUNNY", "CLOUD", "RAINY", "APPLE", "MANGO", "GRAPE",
            "TIGER", "ZEBRA", "MOUSE", "RABBIT", "HOUSE", "CLOCK", "TABLE"
        ]
        self.max_lives = 12
        self.lives = 12


class NineLivesHardMode(NineLives):
    """Hard mode - 7 lives with challenging words"""
    def __init__(self):
        super().__init__()
        self.word_list = [
            "PYTHON", "PROGRAM", "DEVELOPER", "COMPUTER", "ALGORITHM",
            "FUNCTION", "VARIABLE", "DICTIONARY", "DATABASE", "NETWORK",
            "SECURITY", "APPLICATION", "INTERFACE", "SOFTWARE", "HARDWARE",
            "JAVASCRIPT", "TERMINAL", "COMMAND", "PROCESSOR", "MEMORY",
            "ELEPHANT", "GIRAFFE", "KANGAROO", "DOLPHIN", "PENGUIN"
        ]
        self.max_lives = 7
        self.lives = 7


def main():
    """Main menu function"""
    print("""
╔═══════════════════════════════════════╗
║        🐱  NINE LIVES GAME  🐱        ║
╚═══════════════════════════════════════╝
    """)
    
    while True:
        print("\n📋 Select Difficulty:")
        print("1. 🟢 EASY (12 lives, super easy words + hints)")
        print("2. 🟡 NORMAL (9 lives, medium words + hints)")
        print("3. 🔴 HARD (7 lives, challenging words + hints)")
        print("4. ❌ QUIT")
        
        choice = input("\n👉 Enter your choice (1-4): ").strip()
        
        if choice == '1':
            game = NineLivesEasyMode()
            game.play()
        elif choice == '2':
            game = NineLives()
            game.play()
        elif choice == '3':
            game = NineLivesHardMode()
            game.play()
        elif choice == '4':
            print("\n🐱 Goodbye! Thanks for playing Nine Lives! 🐱")
            print("   Come back and save the cat again soon! ❤️")
            sys.exit()
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()