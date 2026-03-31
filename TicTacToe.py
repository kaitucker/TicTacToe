def print_intro():
    """
    Prints the introduction and instructions for Tic-Tac-Toe.
    """
    print("Let's play Tic-Tac-Toe!")
    print("When prompted, enter desired row and column numbers")
    print("Example: 1 3")


def create_board():
    """
    Creates and returns a 3x3 Tic-Tac-Toe board with '_'s as separators.
    
    Returns a 2D list representing the board
    """
    return [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]


def print_board(board):
    """
    Prints the current state of the board in formatted style.
    
    Args:
        board (list): 2D list representing the game board
    """
    for row in board:
        print("| " + " | ".join(row) + " |")


def is_valid_move(board, row, col):
    """
    Checks whether a move is valid.
    
    Args:
        board (list): current game board
        row (int): row index (0–2)
        col (int): column index (0–2)
    
    Returns:
        tuple: (bool, str)
            bool → True if valid, False otherwise
            str → type of error ("bounds", "full", or "")
    """
    # Check if move is within bounds
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False, "bounds"

    # Check if spot is already taken
    if board[row][col] != '_':
        return False, "full"

    return True, ""


def get_move(player, board):
    """
    Prompts the player for input and validates the move.
    
    Args:
        player (str): current player ('X' or 'O')
        board (list): current game board
    
    Returns:
        tuple: valid (row, col) indices
    """
    while True:
        print(f"Enter row and column for player {player}")
        user_input = input().split()

        # Ensure exactly two inputs were given
        if len(user_input) != 2:
            print("Please enter valid row and col numbers from 1 to 3:")
            continue

        # Attempt to convert input to integers
        try:
            row = int(user_input[0]) - 1  # convert to 0-based index
            col = int(user_input[1]) - 1
        except:
            # Input was not integers
            print("Please enter valid row and col numbers from 1 to 3:")
            continue

        # Validate move
        valid, error_type = is_valid_move(board, row, col)

        if not valid:
            if error_type == "bounds":
                print("Please enter valid row and col numbers from 1 to 3:")
            elif error_type == "full":
                print("That spot is full!")
                print("Please enter valid row and col numbers from 1 to 3:")
            continue

        return row, col


def check_win(board, player):
    """
    Checks if the given player has won the game.
    
    Args:
        board (list): current game board
        player (str): 'X' or 'O'
    
    Returns:
        bool: True if player has a winning condition, False otherwise
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    """
    Checks if the board is full (tie condition).
    
    Args:
        board (list): current game board
    
    Returns:
        bool: True if tie, False otherwise
    """
    for row in board:
        if '_' in row:
            return False
    return True


def play_game():
    """
    Runs a single round of Tic-Tac-Toe until win or tie.
    """
    board = create_board()

    print("Let's play!")
    print("Player X starts!")
    print_board(board)

    current_player = 'X'

    # Game loop
    while True:
        # Get valid move from player
        row, col = get_move(current_player, board)

        # Place marker on board
        board[row][col] = current_player
        print_board(board)

        # Check for win
        if check_win(board, current_player):
            print(f"Player {current_player} WINS!")
            return

        # Check for tie
        if check_tie(board):
            print("It's a TIE!")
            return

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


def redo_play_game():
    """
    Controls replay functionality.
    Repeats the game until user chooses 'N'.
    """
    while True:
        play_game()

        # Ask user if they want to play again
        while True:
            print("Do you want to play again? Y or N")
            answer = input().strip().upper()

            if answer == 'Y':
                break
            elif answer == 'N':
                return
            else:
                print("Please enter valid input: Y or N")


def main():
    """
    Main entry point of the program.
    """
    print_intro()
    redo_play_game()


# Ensures main() runs only when script is executed directly
if __name__ == "__main__":
    main()

