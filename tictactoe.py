

## Tic Tac Toe game assignment from Udemy Course ##
#------------------------------------------Initialisations---------------------------------------------#
#board = ['0','1','2','3','4','5','6','7','8','9']
board = [' ']*10
turn = 'Player1'
game_on =True
#---------------------------------------------Functions-----------------------------------------------#
def printBoard(board):
    print ('\t\t{1} | {2} | {3}\n\t\t--|---|--\n\t\t{4} | {5} | {6}\n\t\t--|---|--\n\t\t{7} | {8} | {9}'.format(*board))

def place_marker(board, marker, position):
    board[position] = marker
    

def check_win(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def space_check(board, position):
    return board[position] == ' '

def check_fullboard(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True 


#-----------------------------------------Execution---------------------------------------------------#

marker_p1 = input("Please choose your marker Player 1 (x or o): ")

if marker_p1 == 'x':
    marker_p2 = 'o'
else:
    marker_p2 = 'x'


print("Player1 marker : {0}\tPlayer2 marker : {1}".format(marker_p1,marker_p2))
print('This is the board: \n')
printBoard(board)
print('\n')
print("Player1 to go first\n")



while game_on:

    
    if turn == 'Player1':
        print("Player1 GO!!")
        index = int(input("Select your space [1-9]: "))
        place_marker(board, marker_p1,index)
        printBoard(board)
        
        if check_win(board,marker_p1):
            print("Congratulations Player1. YOU WON !!!")
            game_on = False
        else :
            if check_fullboard(board):
                print("Game is a draw!")
                game_on = False
            else :
                turn = 'Player2'
    else :
        #player 2
        print("Player2 GO!!")
        index = int(input("Select your space [1-9]: "))
        place_marker(board, marker_p2,index)
        printBoard(board)
        
        if check_win(board,marker_p2):
            print("Congratulations Player2. YOU WON !!!")
            game_on = False
        else :
            if check_fullboard(board):
                printBoard(board)
                print("Game is a draw!")
                game_on = False
            else :
                turn = 'Player1'
                


