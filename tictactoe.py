

## Tic Tac Toe game assignment from Udemy Course ##
#------------------------------------------Initialisations---------------------------------------------#
#board = ['0','1','2','3','4','5','6','7','8','9']
board = [' ']*10
p1_result = 'none'
p2_result = 'none'
  
#---------------------------------------------Functions-----------------------------------------------#
def printBoard():
    print ('\t\t{1} | {2} | {3}\n\t\t--|---|--\n\t\t{4} | {5} | {6}\n\t\t--|---|--\n\t\t{7} | {8} | {9}'.format(*board))

def edit_board(self):
    pass

def check_result(marker_p1,marker_p2):
    pass

def write_board():
    pass


#-----------------------------------------Execution---------------------------------------------------#

marker_p1 = input("Please choose your marker Player 1 (x or o): ")

if marker_p1 == 'x':
    marker_p2 = 'o'
else:
    marker_p2 = 'x'


print("Player1 marker : {0}\tPlayer2 marker : {1}".format(marker_p1,marker_p2))
print("Player1 to go first")

while(p1_result!='won' or p1_result!='won'or p1_result!='tie'or p1_result!='tie'):
    print("Player1 GO!!")
    index = int(input("Select your space [1-9]: "))
    write_board
    board[index]=marker_p1
    printBoard()
    check_result(marker_p1,marker_p2)
    print("Player2 GO!!")
    index = int(input("Select your space [1-9]: "))
    write_board
    board[index]=marker_p2
    printBoard()
    check_result(marker_p1,marker_p2)
