class Game:
    def __init__(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def spot_available(self, row, column, player):
        if row < 1 or row > 3 or column < 1 or column > 3:
            print(f"\n{player.name}, please enter a number between 1 and 3.")
            return False
        elif self.board[row - 1][column - 1] == '':
            return True
        else:
            print(f"\n{player.name}, this place is already taken, try again.")
            return False

    def player_play(self, player, row, column):
        self.board[row - 1][column - 1] = player.symbol

    def is_winner(self):
        board = self.board
        # test rows for winner
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return True

        # test columns for winner
        if (board[0][0] == board[1][0] == board[2][0] != "") \
                or (board[0][1] == board[1][1] == board[2][1] != "") \
                or (board[0][2] == board[1][2] == board[2][2] != ""):
            return True

        # test diagonals for winner
        elif (board[0][0] == board[1][1] == board[2][2] != "")\
                or (board[0][2] == board[1][1] == board[2][0] != ""):
            return True
        else:
            return False

    def is_board_full(self):
        if any("" in row for row in self.board):
            return False
        else:
            return True
