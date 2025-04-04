import tictactoe
import player

def printWelcome():
    print("===========================TIC TAC TOE===========================\n")
    print("Welcome to our TicTacToe game !")
    return

def printRules():
    print("You are going to play a TicTacToe game.\n")
    print("Each grid case is represented by a number from 1 to 9.\n")
    print("You can choose to play against a human player or an AI\n")
    print("The board will be shown before each turn\n")

    while True:
            try:
                x=int(input("Do you want to play against a human or player ?\n 1.Human  2.AI\n"))
                if x==1 or x==2:
                    print("Thanks ! May the best win !")
                    return x
                else:
                    print("Please enter a 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def printBye():
    print("Thank you for playing our chess game !\n")
    print("=========================== BYE ===========================\n")
    return

def main():

    player1 = player.Player("Player 1", "X")
    player2 = player.Player("Player 2", "O")
    game = tictactoe.TicTacToe()
    printWelcome()
    x=printRules()
    game.game_logic(player1, player2,x)
    printBye()

if __name__ == "__main__":
    main()