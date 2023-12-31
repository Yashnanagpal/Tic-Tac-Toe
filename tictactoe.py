from sys import exit

def check(board,mark):
    if(board[0][0]==board[0][1]==board[0][2]!='' or board[1][0]==board[1][1]==board[1][2]!='' or board[2][0]==board[2][1]==board[2][2]!='' or board[0][0]==board[1][0]==board[2][0]!='' or board[0][1]==board[1][1]==board[2][1]!='' or board[0][2]==board[1][2]==board[2][2]!='' or board[0][0]==board[1][1]==board[2][2]!='' or board[0][2]==board[1][1]==board[2][0]!=''):
        print(mark,"Wins!")
        exit(0)
    else:
        print("Continue")

def printboard():
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 ")
    
def boardprint(board):
    print(board[0][0] , "|" , board[0][1] , "|" , board[0][2])
    print("--|---|--")
    print(board[1][0] , "|" , board[1][1] , "|" , board[1][2])
    print("--|---|--")
    print(board[2][0] , "|" , board[2][1] , "|" , board[2][2])

def add(board, mark):
    print("Enter the cell number to add ",mark," :")
    cell=int(input())
    row=int(cell/len(board)) 
    column=int(cell%len(board))
    if(board[row][column]==' '):
        board[row][column]=mark
        boardprint(board)
        check(board,mark)
    else:
        print("Already filled")
        add(board,mark)       


print("Welcome to TIC TAC TOE")
print("Check positions of the board")
printboard()
board=[[" ", " ", " "],
       [" ", " ", " "],
       [" ", " ", " "]]
for count in range (9):
    if(count%2 == 0):
        add(board,"X")
    else:
        add(board,"O")
print('Game draw')

