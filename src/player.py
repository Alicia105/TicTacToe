class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def make_a_move(self):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), choose a cell (1-9): "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

"""def main():
    current_player =Player("Player 1", "X")
    print(f"Current player is: {current_player.name}, symbol: {current_player.symbol}")
    print(f"Object methods: {dir(current_player)}")  # Debug: see what methods it has

if __name__ == "__main__":
    main()"""