"""Controller layer - handles game logic and flow"""
import random
import sys
from model import GameState
from views import GameView
from data import (
    WORD_CATEGORIES, EASY_CATEGORIES, HARD_CATEGORIES,
    get_word_with_category, get_hint_for_word
)

class GameController:
    """Controls the game flow and logic"""
    
    def __init__(self, difficulty="normal"):
        self.difficulty = difficulty
        self.view = GameView()
        self.game_state = None
        
        # Set up difficulty parameters
        if difficulty == "easy":
            self.categories = EASY_CATEGORIES
            self.max_lives = 12
            self.category_names = list(EASY_CATEGORIES.keys())
        elif difficulty == "hard":
            self.categories = HARD_CATEGORIES
            self.max_lives = 7
            self.category_names = list(HARD_CATEGORIES.keys())
        else:  # normal
            self.categories = WORD_CATEGORIES
            self.max_lives = 9
            self.category_names = list(WORD_CATEGORIES.keys())
    
    def setup_new_game(self):
        """Setup a new game with random word and category"""
        # Choose random category
        category_name = random.choice(self.category_names)
        
        # Get word from that category
        word, category, icon, hint_prefix = get_word_with_category(
            self.categories, category_name
        )
        
        # Create game state
        self.game_state = GameState(
            secret_word=word,
            category=category,
            category_icon=icon,
            hint_prefix=hint_prefix,
            max_lives=self.max_lives
        )
        
        # Show category hint at start
        self.view.show_category_hint(self.game_state)
    
    def process_letter_guess(self, letter):
        """Process a letter guess"""
        self.game_state.guessed_letters.add(letter)
        
        if letter in self.game_state.secret_word:
            count = self.game_state.reveal_letter(letter)
            self.view.show_letter_result(letter, True, count, self.game_state)
            return True
        else:
            self.game_state.lose_life(1)
            self.view.show_letter_result(letter, False, 0, self.game_state)
            return False
    
    def process_word_guess(self, word):
        """Process a full word guess"""
        if word == self.game_state.secret_word:
            self.game_state.reveal_letter(word)  # Reveal all letters
            self.view.show_word_result(word, True, self.game_state)
            self.game_state.win_game()
            return True
        else:
            self.game_state.lose_life(2)
            self.view.show_word_result(word, False, self.game_state)
            return False
    
    def handle_hint(self):
        """Provide a hint to the player"""
        hint_text = get_hint_for_word(
            self.game_state.secret_word,
            self.game_state.hint_prefix,
            self.game_state.category
        )
        self.view.show_hint(hint_text)
    
    def play_round(self):
        """Play one round of the game"""
        self.setup_new_game()
        
        while not self.game_state.game_over:
            self.view.show_game_state(self.game_state)
            
            guess, guess_type = self.view.get_player_guess(self.game_state)
            
            if guess_type == "hint":
                self.handle_hint()
            elif guess_type == "letter":
                self.process_letter_guess(guess)
                if self.game_state.is_word_revealed():
                    self.game_state.win_game()
            else:  # word guess
                self.process_word_guess(guess)
            
            # Check win/loss conditions
            if self.game_state.won:
                self.view.show_victory(self.game_state)
                break
            elif self.game_state.game_over and not self.game_state.won:
                self.view.show_defeat(self.game_state)
                break
    
    def run(self):
        """Main game loop"""
        self.view.show_welcome()
        
        while True:
            self.play_round()
            
            if not self.view.ask_play_again():
                self.view.show_goodbye()
                sys.exit()