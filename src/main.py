import tictactoe
import player

def main():

    player1 = player.Player("Player 1", "X")
    player2 = player.Player("Player 2", "O")
    game = tictactoe.TicTacToe()
    game.game_logic(player1, player2)

if __name__ == "__main__":
    main()