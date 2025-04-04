import player
class TicTacToe:

    def __init__(self):
        self.numberOfTurn=0
        #self.currentPlayer="X"
        self.board=[["1","2","3"],
                    ["4","5","6"],
                    ["7","8","9"]]
        self.positions=dict()

    def get_board(self):
        return self.board

    #good
    def print_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 10)

    #good
    def check_winner(self, symbol):
        b = self.board
        for i in range(3):
            if all(b[i][j] == symbol for j in range(3)) or \
            all(b[j][i] == symbol for j in range(3)):
                return True
        if all(b[i][i] == symbol for i in range(3)) or \
        all(b[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    #good
    def is_board_full(self):
        return len(self.positions) == 9
    
    #good
    def update_board(self, move, symbol):
        self.positions[move] = symbol
        row = (move - 1) // 3
        col = (move - 1) % 3
        self.board[row][col] = symbol

    #good   
    def game_human(self, player1, player2):
        while not self.is_board_full():
            self.print_board()

            # PLAYER 1 TURN
            while True:
                move = player1.make_a_move()
                if not self.positions.get(move):
                    break
                print("That cell is already taken. Try again.")

            self.update_board(move, player1.get_symbol())
            if self.check_winner(player1.get_symbol()):
                self.print_board()
                print(f"{player1.name} wins!")
                return

            if self.is_board_full():
                break  # Prevents asking player2 for a move after last cell

            self.print_board()

            # PLAYER 2 TURN
            while True:
                move = player2.make_a_move()
                if not self.positions.get(move):
                    break
                print("That cell is already taken. Try again.")

            self.update_board(move, player2.get_symbol())
            if self.check_winner(player2.get_symbol()):
                self.print_board()
                print(f"{player2.name} wins!")
                return

            self.numberOfTurn += 1

        self.print_board()
        print("It's a draw!")

    def game_logic(self, player1, player2,selector):
        if selector==1:
            self.game_human(player1,player2)
        if selector==2:
            return
