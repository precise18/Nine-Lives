from controllers import GameController
from views import GameView

def main():
    """Main function to run the game"""
    view = GameView()
    
    while True:
        choice = view.show_difficulty_menu()
        
        if choice == '1':
            game = GameController(difficulty="easy")
            game.run()
        elif choice == '2':
            game = GameController(difficulty="normal")
            game.run()
        elif choice == '3':
            game = GameController(difficulty="hard")
            game.run()
        elif choice == '4':
            view.show_goodbye()
            break

if __name__ == "__main__":
    main()