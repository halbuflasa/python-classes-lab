class Game:
    def __init__(self, turn='X', tie=False, winner=None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                return move
            print("Invalid move. Please try again.")

    def check_for_winner(self):
        winning_combinations = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['c1', 'b2', 'a3'],
        ]
        for combo in winning_combinations:
            if all(self.board[pos] == self.turn for pos in combo):
                self.winner = self.turn
                return True
        return False

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True
            return True
        return False

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Player X goes first.")
        print("Use the format 'A1', 'B2', etc., to make a move.")
        while not self.winner and not self.tie:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn
            if self.check_for_winner():
                self.render()
                print(f"Congratulations! {self.turn} wins!")
                break
            if self.check_for_tie():
                self.render()
                print("It's a tie!")
                break
            self.switch_turn()

if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
