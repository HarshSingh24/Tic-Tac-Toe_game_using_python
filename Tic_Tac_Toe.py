def display(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    
    
def player_input():
    
    '''
    OUTPUT = (Player1 marker, Player2 marker)
    '''
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1 choose X or O: ').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
    
def place_marker(board,marker,position):
    
    board[position] = marker
    
    
def win_check(board,mark):
    
    return((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or 
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or 
    (board[7] == board[5] == board[3] == mark) or 
    (board[9] == board[5] == board[1] == mark))


import random

def choose_first():
    
    choice = random.randint(0,1)
    
    if choice == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
    
def space_check(board,position):
    
    return board[position] == ' '
    
    
def full_boardcheck(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a position (1-9): "))
        
    return position
    

def replay():
    choice = input("Play again ? Enter Y or N: ")
    
    return choice == 'Yes'



print("Welcome To TIC TAC TOE")

while True:
    
    board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? yes or no: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
            
            display(board)
            
            position = player_choice(board)
            
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                display(board)
                print('HURRAY! PLAYER 1 HAS WON 😊')
                game_on = False
                
            else:
                if full_boardcheck(board):
                    display(board)
                    print('GAME TIED 🤦‍')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            
            display(board)
            
            position = player_choice(board)
            
            place_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                display(board)
                print('HURRAY! PLAYER 2 HAS WON 😊')
                game_on = False
                
            else:
                if full_boardcheck(board):
                    display(board)
                    print('GAME TIED 🤦‍')
                    game_on = False
                else:
                    turn = 'Player 1'
                    
                    
    if not replay():
        break
                