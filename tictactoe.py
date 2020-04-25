#----- Global variable ------
import random
#game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
game_still_going = True
#who won 
winner = None
#whos Turn is this 
current_player = "X"
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])    
#play a game of tic tac toe
def play_game():
    display_board() #display initial board
    while game_still_going:
        
        #handle a single turn
        handle_turn(current_player)
        
        #check if game is over 
        check_if_game_over()
        
        # flip to the other player 
        flip_player()
    #the game ended
    if(winner=="X" or winner=="O"):
        print(winner + " won.")
    else:
        print("Tie.")
#handle a single turn
def handle_turn(player):
    if(player=="X"):
        position = input("Choose from 1-9 : ")
        position = int(position) -1
        while(board[position]!="-" or (position < 0 or position > 10)):
            print("Enter again that position was filled")
            position = input("Choose again from 1-9 : ")
            position = int(position) -1
        
        board[position] = player
        display_board() 
        
    elif(player=="O"):
        position = random.randint(1,9)
        position =position -1
        while(board[position]!="-"):
            position = random.randint(1,9)
            position =position -1
        board[position] = player
        print("Computer chooses " + str(position+1) + " position")
        display_board() 
            
            

def check_if_game_over():
    check_if_win()
    check_if_tie()
    
def check_if_win():
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagnols_winner = check_diagnols()
    if(row_winner):
        #there was a win
        winner=row_winner
    elif(column_winner):
        #there was a win
        winner=column_winner
    elif(diagnols_winner):
        #there was a win
        winner = diagnols_winner
    else:
        #there was no win 
        winner = None
    return
def check_rows():
    #setup a global variable
    global game_still_going
    row_1 = board[0]==board[1]==board[2] != "-"
    row_2 = board[3]==board[4]==board[5] != "-"
    row_3 = board[6]==board[7]==board[8] != "-"
    if(row_1 or row_2 or row_3):
        game_still_going = False
    #returning the winner
    if(row_1):
        return board[0]
    if(row_2):
        return board[3]
    if(row_3):
        return board[6]

def check_columns():
    #check columns 
    global game_still_going
    col_1 = board[0]==board[3]==board[6] != "-"
    col_2 = board[1]==board[4]==board[7] != "-"
    col_3 = board[2]==board[5]==board[8] != "-"
    if(col_1 or col_2 or col_3):
        game_still_going = False
    #returning the winner
    if(col_1):
        return board[0]
    if(col_2):
        return board[1]
    if(col_3):
        return board[2]
    return

def check_diagnols():
    #check diagnols 
    global game_still_going
    diag_1 = board[0]==board[4]==board[8] != "-"
    diag_2 = board[2]==board[4]==board[6] != "-"
    if(diag_1 or diag_2):
        game_still_going = False
    #returning the winner
    if(diag_1):
        return board[0]
    if(diag_2):
        return board[2]
    return 

    
def check_if_tie():
    #check if there is a tie or not
    global game_still_going
    if("-" not in board):
        game_still_going = False
    
    return 

def flip_player():
    # flip the player after X turns 
    global current_player
    if(current_player=="X"):
        current_player="O"
    elif(current_player=="O"):
        current_player="X"
    
    return 

play_game()
