"""
Author:         Kai Tucker
Date:           3/26/26
Assignment:     Project 1
Course:         CPSC1050
Lab Section:    02

Code Description: Creates and runs a game of Tic-Tac-Toe for the user to play
"""

def print_intro():
    """
    Prints an introduction and example board.
    """
    print("Let's play Tic-Tac-Toe!")
    print("When prompted, enter desired row and column numbers")
    print("Example: 1 3")

    #Example board
    print("| _ | _ | X |")
    print("| _ | _ | _ |")
    print("| _ | _ | _ |")


def create_board():
    """
    Creates and returns a 3x3 Tic-Tac-Toe board with '_'s as breakers.
    
    Returns a 2D list representing the board
    """
    return [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]


def print_board(board):
    """
    Prints the current state of the board in formatted style.
    
    Args:
        -board (list): 2D list representing the game board
    """
    for row in board:
        print("| " + " | ".join(row) + " |")


def is_valid_move(board, row, col):
    """
    Checks whether a move is valid and returns a tuple with the result.
    
    Args:
        board (list): current game board
        row (int): row index (0–2)
        col (int): column index (0–2)
    
    Returns:
        tuple: (bool, str)
            For the bool, its True if valid, and False otherwise
            FOr the string, it gives the type of error ("bounds", "full", or "")
    """
    #Checks if move is within bounds
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False, "bounds"

    #Checks if the inputted spot is already taken
    if board[row][col] != '_':
        return False, "full"

    return True, ""


def get_move(player, board):
    """
    Prompts the player for input and validates the given player move.
    (No while True here :))
    """
    valid_move = False

    while not valid_move:
        print(f"Enter row and column for player {player}")
        user_input = input().split()

        #Checks lengths of input
        if len(user_input) != 2:
            print("Please enter valid row and col numbers from 1 to 3:")
            continue

        #Checks if both inputs are integers
        if not (user_input[0].isdigit() and user_input[1].isdigit()):
            print("Please enter valid row and col numbers from 1 to 3:")
            continue

        row = int(user_input[0]) - 1
        col = int(user_input[1]) - 1

        #Bounds check of 1 to 3
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Please enter valid row and col numbers from 1 to 3:")
            continue

        #Spots taken check
        if board[row][col] != '_':
            print("That spot is full!")
            print("Please enter valid row and col numbers from 1 to 3:")
            continue

        #If all checks pass
        valid_move = True

    return row, col


def check_win(board, player):
    """
    Checks if the given player has won the game.
    
    Args:
        board (list): current game board
        player (str): 'X' or 'O'
    
    Returns:
        boolena: True if player has a winning condition, False otherwise
    """
    #Checks rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    #Checks columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    #Checks diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    """
    Checks if the board is full.
    
    Args:
        board (list): current game board
    
    Returns:
        boolean: True if tie, False otherwise
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

    #Loop for the game
    while True:
        # Get valid move from player
        row, col = get_move(current_player, board)

        #Place tile on the board
        board[row][col] = current_player
        print_board(board)

        #Checks for a win
        if check_win(board, current_player):
            print(f"Player {current_player} WINS!")
            return

        #Checks for a tie
        if check_tie(board):
            print("It's a TIE!")
            return

        #Switch player turn
        current_player = 'O' if current_player == 'X' else 'X'


def redo_play_game():
    """
    Controls how the game replays
    """
    play_again = True

    while play_again:
        play_game()

        valid_input = False

        while not valid_input:
            print("Do you want to play again? Y or N")
            answer = input().strip().upper()

            if answer == 'Y':
                print("Let's play!")
                valid_input = True
            elif answer == 'N':
                play_again = False
                valid_input = True
            else:
                print("Please enter valid input: Y or N")


def main():
    """
    Program starter
    """
    print_intro()
    redo_play_game()


#Runs the program when the script is called
if __name__ == "__main__":
    main()