from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7],'|',board[8],'|',board[9])
    print('---------')
    print(board[4],'|',board[5],'|',board[6])
    print('---------')
    print(board[1],'|',board[2],'|',board[3])

def player_input():
    marker='wrong'
    while not (marker =='X' or marker == 'O' ):
        marker = input("Player 1: Do you want to be X or O ?").upper()
        
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,marker):
    winning_combo=[(7,8,9),(4,5,6),(1,2,3),  #horizontal
                   (7,4,1),(8,5,2),(9,6,3),  #vertical
                   (9,5,1),(7,5,3)]          #diagnol

    for combo in winning_combo:
        if board[combo[0]]==board[combo[1]]==board[combo[2]]==marker:
            return True
    return False

import random
def choose_first():
    random_number=random.randint(0,1)
    if random_number==0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board,position): 
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
            
    #board is full if we return true
    return True

def player_choice(board):
    position=0
    
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Choose where you want to place your marker(1-9):'))
    
    return position
 

def replay():
    choice=input("Play again ? Yes or No ")
    return choice == 'Yes'

#WHILE LOOP TO KEEP RUNNNG THE GAME
print("Welcome to Tic Tac Toe")

while True:
    #PLAY THE GAME
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()

    turn=choose_first()
    print(turn + 'will go first')

    play_game= input('Ready to play ? Y or N: ').upper()
    if play_game=='Y':
        game_on = True
    else:
        game_on = False
        
    ## GAME PLAY

    while game_on:
        if turn=='Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            ##CHECK IF THEY WON
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON !!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('ITS A TIE !!')
                    game_on=False
                else:
                    turn = 'Player 2'
###### PLAYER 2ND TURN ##############
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON !!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('ITS A TIE !!')
                else:
                    turn= 'Player 1'
   
    if not replay():
        break
        
    
