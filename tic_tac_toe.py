from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7],'|',board[8],'|',board[9])
    print('---------')
    print(board[4],'|',board[5],'|',board[6])
    print('---------')
    print(board[1],'|',board[2],'|',board[3])
    
def player_input():
    marker='wrong'
    while marker not in ('X', 'O'):
        marker = input("Player 1: Do you want to be X or O? ").upper()
    return ('X', 'O') if marker == 'X' else ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    winning_combos = [(7,8,9), (4,5,6), (1,2,3), (7,4,1), (8,5,2), (9,6,3), (9,5,1), (7,5,3)]
    return any(board[a] == board[b] == board[c] == marker for a, b, c in winning_combos)

def choose_first():
    return 'Player 1' if random.randint(0,1) == 0 else 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(space_check(board, i) == False for i in range(1, 10))

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        try:
            position = int(input('Choose where to place your marker (1-9): '))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    return position

def replay():
    return input("Play again? Yes or No: ").strip().lower() == 'yes'

print("Welcome to Tic Tac Toe!")

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Ready to play? Y or N: ').strip().upper()
    game_on = play_game == 'Y'
    
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                display_board(board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("IT'S A TIE!!")
                game_on = False
            else:
                turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                display_board(board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("IT'S A TIE!!")
                game_on = False
            else:
                turn = 'Player 1'
    
    if not replay():
        break
