from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print("{}|{}|{}".format(board[0],board[1],board[2]))
    print("-----")
    print("{}|{}|{}".format(board[3],board[4],board[5]))
    print("-----")
    print("{}|{}|{}".format(board[6],board[7],board[8]))

def status(board):
    if board.count("X") + board.count("O") == 9:
        return True
    else:
        return False
    
def win(board):
    a = (board[0] == board[1] == board[2] == "X") or (board[0] == board[1] == board[2] == "O")
    b = (board[3] == board[4] == board[5] == "X") or (board[3] == board[4] == board[5] == "O")
    c = (board[6] == board[7] == board[8] == "X") or (board[6] == board[7] == board[8] == "O")
    d = (board[0] == board[3] == board[6] == "X") or (board[0] == board[3] == board[6] == "O")
    e = (board[1] == board[4] == board[7] == "X") or (board[1] == board[4] == board[7] == "O")
    f = (board[2] == board[5] == board[8] == "X") or (board[2] == board[5] == board[8] == "O")
    g = (board[0] == board[4] == board[8] == "X") or (board[0] == board[4] == board[8] == "O")
    h = (board[2] == board[4] == board[6] == "X") or (board[2] == board[4] == board[6] == "O")
                                                      
    return a or b or c or d or e or f or g or h
    

print("Welcome to Tic Tac Toe!\n")

board = ["#"]*9

player_1 = input("Player One: Please choose your marker X or O: ")

while player_1 not in ["X","O"]:
    player_1 = input("Wrong Choice Player One: Please choose your marker X or O: ")
    
if player_1 == "X":
    player_2 = "O"
else:
    player_2 = "X"

print("Player One: Your marker is {}\n".format(player_1))
print("Player Two: Your marker is {}\n".format(player_2))

display_board(board)

while (not status(board)) and (not(win(board))):
    
    count = board.count("X") + board.count("O")
    
    if count % 2 == 0:
    
        board_position = int( input("Please enter a number for the board position choice Player 1: ") )

        while board_position not in [1,2,3,4,5,6,7,8,9]:
            board_position = int( input("Wrong Entry, Please enter a valid number for the board position choice Player 1: "))
        
        while board[board_position -1] != "#":
            board_position = int( input("Invalid, Please enter a valid number for the board position choice Player 1: "))
        
        board[board_position -1] = player_1
            
    else:
        board_position = int(input("Please enter a number for the board position choice Player 2: "))

        while board_position not in [1,2,3,4,5,6,7,8,9]:
            board_position = int(input("Please enter a number for the board position choice Player 2: "))
        
        while board[board_position -1] != "#":
            board_position = int( input("Invalid, Please enter a valid number for the board position choice Player 2: "))  
        
        board[board_position -1] = player_2
    
    display_board(board)
    
if status(board):
    print("Nobody wins, it's a draw")
elif win(board):
    count = board.count("X") + board.count("O")
    
    if count % 2 != 0:
        print("Congratulations Player One, You Win!")
    else:
        print("Congratulations Player Two, You Win!")
        
    
