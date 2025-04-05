from tkinter import *
from tkinter import messagebox
from tictactoe import *
from player import *
import random

class TicTacToeGUI(TicTacToe):

    def __init__(self, window):
        super().__init__()

        self.window = window
        self.ai_turn = None
        self.game_mode = None  # 'ai' or 'human'
        self.numberOfTurn = 0  # Track turns for both human and AI
        # Ask for game mode
        self.ask_game_mode()
        
        self.window.title("TicTacToe AI")
        self.window.geometry('500x500')
        self.window['bg'] = 'white'
        self.window.resizable(width=True, height=True)

        self.buttons = []

        # Create 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                button = Button(window, text="", width=10, height=5, font=("Verdana", 12), fg="black", bg="white", command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def ask_game_mode(self):
        choice_window = Toplevel(self.window)
        choice_window.title("Choose Opponent")
        choice_window.geometry("300x150")
        choice_window.grab_set()

        Label(choice_window, text="Choose your opponent:", font=("Verdana", 12)).pack(pady=10)

        Button(choice_window, text="Play against AI", width=15, command=lambda: self.set_game_mode('ai', choice_window)).pack(pady=5)
        Button(choice_window, text="Play against Human", width=15, command=lambda: self.set_game_mode('human', choice_window)).pack(pady=5)

    def set_game_mode(self, mode, window):
        self.game_mode = mode
        window.destroy()
        print(f"Selected game mode: {mode}")

        if mode == 'ai':
            self.ai_turn = random.choice([True, False])  # Randomly decide if AI starts or not
            if self.ai_turn:
                self.aiPlayer = 'X'
                self.humanPlayer = 'O'
            else:
                self.aiPlayer = 'O'
                self.humanPlayer = 'X'

    def ai_move(self):
        move = self.get_best_move()
        if move is None:
            return
        self.update_board(move, self.aiPlayer)
        row = (move - 1) // 3
        col = (move - 1) % 3
        self.update_button_text(row, col, self.aiPlayer)

        if self.check_winner(self.aiPlayer):
            messagebox.showinfo("Game Over", "AI wins!")
            self.window.quit()
            return

        if self.is_board_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.window.quit()

        self.ai_turn = False  # Switch to human after AI's turn

    def update_button_text(self, i, j, symbol):
        idx = i * 3 + j
        self.buttons[idx].config(text=symbol)

    def on_click(self, i, j):
        move = i * 3 + j + 1
        if self.positions.get(move):  # Cell already taken
            return

        if self.game_mode == 'human':
            current_symbol = 'X' if self.numberOfTurn % 2 == 0 else 'O'
            self.update_board(move, current_symbol)
            self.update_button_text(i, j, current_symbol)

            if self.check_winner(current_symbol):
                messagebox.showinfo("Game Over", f"{'Player 1' if current_symbol == 'X' else 'Player 2'} wins!")
                self.window.quit()
                return

            if self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
                return

            self.numberOfTurn += 1

        elif self.game_mode == 'ai':
            # Human's turn
            if not self.ai_turn:  # If it's human's turn
                current_symbol = 'X' if self.numberOfTurn % 2 == 0 else 'O'
                self.update_board(move, current_symbol)
                self.update_button_text(i, j, current_symbol)

                if self.check_winner(current_symbol):
                    messagebox.showinfo("Game Over", f"You win!")
                    self.window.quit()
                    return

                if self.is_board_full():
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.window.quit()
                    return

                self.numberOfTurn += 1

                # After the human move, it's now the AI's turn
                self.ai_turn = True
                self.window.after(300, self.ai_move)  # AI makes its move after a short delay
            else:
                return  # Do nothing if it's AI's turn

def main():
    player1 = player.Player("Player 1", "X")
    player2 = player.Player("Player 2", "O")
    window = Tk()
    game = TicTacToeGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()
