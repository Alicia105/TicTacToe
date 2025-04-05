import player
# Randomly decide who goes first
import random
class TicTacToe:

    def __init__(self):
        self.numberOfTurn=0
        self.aiPlayer=""
        self.humanPlayer=""
        self.positions=dict()
        self.board=[[1,2,3],
                    [4,5,6],
                    [7,8,9]]

    def get_board(self):
        return self.board

    #good
    def print_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print(" | ".join(str(cell) for cell in row))
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
            return
        if selector==2:
            self.game_ai(player1)
            return
   
    #good 
    def is_empty(self,i,j):
        if self.board[i][j]!='X' and self.board[i][j]!='O':
            return True
        return False
    
    #good 
    def get_all_possible_moves(self):
        moves=[]
        for i in range(3):
            for j in range(3):
                if self.is_empty(i,j):
                    moves.append(self.board[i][j])
        return moves
    
    def game_over(self):
       return self.check_winner('X') or self.check_winner('O') or self.is_board_full()
    
    def undo_move(self, move):
        row = (move - 1) // 3
        col = (move - 1) % 3
        self.board[row][col] = move
        if move in self.positions:
            del self.positions[move]

    def minimax(self, depth, is_maximizing):
       """
       Minimax algorithm implementation
       Returns the best score possible for the current board state
       """
       # Base cases

       #if human player wins
       if self.check_winner(self.humanPlayer):
           return -1
       #if ai player wins
       if self.check_winner(self.aiPlayer):
           return 1
       if self.is_board_full():
           return 0
 
        # if it is the maximizing player's turn (AI), we want to maximize the score
       if is_maximizing:
            best_score = float("-inf")
            for move in self.get_all_possible_moves():
                # Make a calculating move
                self.update_board(move,self.aiPlayer)
                # Recursively call minimax with the next depth and the minimizing player
                score = self.minimax(depth + 1, False)
                # Reset the move
                self.undo_move(move)
                # Update the best score
                best_score = max(score, best_score)
            return best_score
       else:
            # if it is the minimizing player's turn (human), we want to minimize the score
            best_score = float("inf")
            for move in self.get_all_possible_moves():
                # Make a calculating move
                self.update_board(move,self.humanPlayer)
                # Recursively call minimax with the next depth and the maximizing player
                score = self.minimax(depth + 1, True)
                # Reset the move
                self.undo_move(move)
                # Update the best score
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
       """Find the best move for AI using minimax"""
       best_score = float("-inf")
       best_move = None

       for move in self.get_all_possible_moves():
           # Make a calculating move
           self.update_board(move,self.aiPlayer)
           # Recursively call minimax with the next depth and the minimizing player
           score = self.minimax(0, False)
           # Reset the move
           self.undo_move(move)
           # Update the best score
           if score > best_score:
               best_score = score
               best_move = move

       return best_move
   
    def game_ai(self,player1): 

        ai_turn = random.choice([True, False])

        if ai_turn:
                self.aiPlayer='X'
                self.humanPlayer='O'
                player1.set_symbol(self.humanPlayer)
        else:
                self.aiPlayer='O'
                self.humanPlayer='X'
                player1.set_symbol(self.humanPlayer)

        while not self.is_board_full():
            self.print_board()

            if ai_turn:
                print(f"\nAI's turn({self.aiPlayer})...\n")
                move = self.get_best_move()
                self.update_board(move,self.aiPlayer)
                if self.check_winner(self.aiPlayer):
                    self.print_board()
                    print("\nAI wins !\n")
                    return

                if self.is_board_full():
                    break  # Prevents asking player2 for a move after last cell

                self.print_board()
            else:
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

                    self.numberOfTurn += 1 


            ai_turn = not ai_turn

        self.print_board()
        print("It's a draw!")

