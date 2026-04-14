from art import get_hangman_art, display_title
class GameView:
    """Handles all display and user interaction"""
    
    @staticmethod
    def show_welcome():
        """Display welcome screen"""
        display_title()
    
    @staticmethod
    def show_difficulty_menu():
        """Display difficulty selection menu"""
        print("\n📋 Select Difficulty:")
        print("1. 🟢 EASY (12 lives, simple words + category hints)")
        print("2. 🟡 NORMAL (9 lives, medium words + category hints)")
        print("3. 🔴 HARD (7 lives, challenging words + category hints)")
        print("4. ❌ QUIT")
        
        while True:
            choice = input("\n👉 Enter your choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
    
    @staticmethod
    def show_game_state(game_state):
        """Display current game state"""
        print("\n" + "="*50)
        print(f"❤️  LIVES: {'❤️ ' * game_state.lives}".rjust(30))
        print(f"📂 CATEGORY: {game_state.category_icon} {game_state.category}")
        print("="*50)
        print(f"\n📝 WORD: {' '.join(game_state.hidden_word)}")
        print(f"🎯 GUESSED LETTERS: {', '.join(sorted(game_state.guessed_letters)) if game_state.guessed_letters else 'None'}")
        print(f"💀 LIVES REMAINING: {game_state.lives}/{game_state.max_lives}")
        
        # Show hangman art
        print(get_hangman_art(game_state.lives, game_state.max_lives))
    
    @staticmethod
    def show_category_hint(game_state):
        """Show the category hint to the player"""
        print(f"\n📂 CATEGORY HINT: This word is from the **{game_state.category}** category! {game_state.category_icon}")
    
    @staticmethod
    def get_player_guess(game_state):
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
                if guess in game_state.guessed_letters:
                    print(f"⚠️  You already guessed '{guess}'. Try a different letter!")
                    continue
                return guess, "letter"
            else:
                return guess, "word"
    
    @staticmethod
    def show_letter_result(letter, found, count, game_state):
        """Show result of a letter guess"""
        if found:
            print(f"✅ Good guess! '{letter}' appears {count} time(s) in the word!")
        else:
            print(f"❌ Sorry! '{letter}' is not in the word. You lose a life!")
            print(f"💔 {game_state.lives} lives remaining")
    
    @staticmethod
    def show_word_result(guess, correct, game_state):
        """Show result of a word guess"""
        if correct:
            print(f"\n🎉 AMAZING! '{guess}' IS THE WORD! 🎉")
        else:
            print(f"❌❌ Wrong word! '{guess}' is not the secret word. You lose 2 lives!")
            print(f"💔 {game_state.lives} lives remaining")
    
    @staticmethod
    def show_victory(game_state):
        """Show victory message"""
        print(f"\n🌟 CONGRATULATIONS! YOU SAVED THE CAT! 🌟")
        print(f"🏆 You guessed the word '{game_state.secret_word}' from the {game_state.category} category with {game_state.lives} lives remaining! 🏆")
    
    @staticmethod
    def show_defeat(game_state):
        """Show defeat message"""
        print(f"\n💀 GAME OVER! 💀")
        print(f"😭 The cat ran out of lives... The word was '{game_state.secret_word}' from the {game_state.category} category")
    
    @staticmethod
    def show_hint(hint_text):
        """Display a hint"""
        print(f"\n{hint_text}")
    
    @staticmethod
    def ask_play_again():
        """Ask if player wants to play again"""
        while True:
            choice = input("\n🐱 Play again? (yes/no): ").lower().strip()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n']:
                return False
            print("Please enter 'yes' or 'no'")
    
    @staticmethod
    def show_goodbye():
        """Display goodbye message"""
        print("\n🐱 Thanks for playing Nine Lives! Meow! 🐱")
        print("   Come back and save the cat again soon! ❤️")