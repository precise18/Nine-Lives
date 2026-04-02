import random
import sys

class NineLives:
    def __init__(self):
        self.word_list = [
            "Elephant", "Lioness", "Leopard", "Giraffe", "Hippopotamus",
            "Chickens", "Dolphins", "Whale", "Kangaroo", "Baboon",
            "Rhinoceros", "Peacock", "Crocodile", "Cheetah", "Hyena",
            "Tortoise", "Chameleon", "Octopus", "Jellyfish", "Eagle"
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
            guess = input("\n🔤 Enter a letter or word: ").upper().strip()
            
            if not guess:
                print("❌ Please enter something!")
                continue
                
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
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.hidden_word[i] = letter
            print(f"✅ Good guess! '{letter}' is in the word!")
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
║   Can you save the cat? 🐱❤️          ║
╚═══════════════════════════════════════╝
        """)
        
        self.choose_word()
        
        while True:
            self.display_game_state()
            self.display_hangman()
            
            guess, guess_type = self.get_player_guess()
            
            if guess_type == "letter":
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


class NineLivesHardMode(NineLives):
    """Hard mode version - more difficult word list"""
    def __init__(self):
        super().__init__()
        self.word_list = [
            "XYLOPHONE", "JAZZ", "ZEPHYR", "QUIXOTIC", "SYNCHRONIZE",
            "LYMPHATIC", "DWARVES", "MYSTIFY", "OXIDIZE", "WHISPERING",
            "ZODIAC", "QUARTZ", "JUXTAPOSE", "EXORCISM", "HYDROXYZINE"
        ]
        self.max_lives = 7
        self.lives = 7


class NineLivesEasyMode(NineLives):
    """Easy mode version - shorter words"""
    def __init__(self):
        super().__init__()
        self.word_list = [
            "CAT", "DOG", "FISH", "BIRD", "MOON",
            "SUN", "STAR", "TREE", "FLOWER", "HOUSE",
            "CAR", "BOOK", "PEN", "HAT", "SHOE"
        ]
        self.max_lives = 12
        self.lives = 12


def main():
    """Main menu function"""
    print("""
╔═══════════════════════════════════════╗
║        🐱  NINE LIVES GAME  🐱        ║
╚═══════════════════════════════════════╝
    """)
    
    while True:
        print("\nSelect difficulty:")
        print("1. 🟢 EASY (12 lives, short words)")
        print("2. 🟡 NORMAL (9 lives, medium words)")
        print("3. 🔴 HARD (7 lives, challenging words)")
        print("4. ❌ QUIT")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
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
            print("\n🐱 Goodbye! Thanks for playing! 🐱")
            sys.exit()
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()