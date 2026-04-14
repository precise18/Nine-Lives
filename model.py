class GameState:
    """Represents the state of a game session"""
    def __init__(self, secret_word, category, category_icon, hint_prefix, max_lives=9):
        self.secret_word = secret_word
        self.category = category
        self.category_icon = category_icon
        self.hint_prefix = hint_prefix
        self.hidden_word = ['_' for _ in secret_word]
        self.lives = max_lives
        self.max_lives = max_lives
        self.guessed_letters = set()
        self.game_over = False
        self.won = False
    
    def reveal_letter(self, letter):
        """Reveal a letter in the hidden word, return number of occurrences"""
        count = 0
        for i, char in enumerate(self.secret_word):
            if char == letter:
                self.hidden_word[i] = letter
                count += 1
        return count
    
    def is_word_revealed(self):
        """Check if the entire word has been revealed"""
        return '_' not in self.hidden_word
    
    def lose_life(self, amount=1):
        """Lose lives, return True if game over"""
        self.lives -= amount
        if self.lives <= 0:
            self.game_over = True
            return True
        return False
    
    def win_game(self):
        """Mark game as won"""
        self.won = True
        self.game_over = True