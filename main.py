from tabulate import tabulate
from game import Game
from player import Player
from art import art


game = Game()
player_1 = Player('X', 'Player 1')
player_2 = Player('0', 'Player 2')

active_player = player_1


def change_player():
    global active_player
    active_player = player_2 if active_player == player_1 else player_1


game_is_on = True
print(art)

while game_is_on:
    # ask active player for input, replay if player selects a position that's taken or out of the board
    is_available = False
    while not is_available:
        row = int(input(f"\n{active_player.name} ('{active_player.symbol}'), please select a row (1, 2 or 3)? "))
        column = int(input(f"{active_player.name} ('{active_player.symbol}'), please select a column (1, 2 or 3)? "))
        if game.spot_available(row, column, active_player):
            game.player_play(active_player, row, column)
            is_available = True
            print(tabulate(game.board, tablefmt="grid"))

    # check if active player is winner
    if game.is_winner():
        print(f"\nCongratulations {active_player.name}, you win!")
        game_is_on = False

    # check if board is full
    if game.is_board_full():
        print("\nThe board is full, this is a draw!")
        game_is_on = False

    change_player()
