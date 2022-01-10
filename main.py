from game import Game

new_game = Game()
while new_game.running:
    new_game.current_menu.display_menu()
    new_game.game_loop()
