import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    print(" -----------")
    for i in range(3):
        print("| "+ board[i][0] + " | " + board[i][1] + " | " + board[i][2] + " |")
        print(" -----------")
    pass

def welcome(board):
    # prints the welcome message
    print("\nWelcome to the Unbeateable Noughts and Crosses.")
    print("The board layout is shown below.")
    # display the board by calling draw_board(board)
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")
    pass

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(len(board)):
        board[i][0] = " "
        board[i][1] = " "
        board[i][2] = " "
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    print("                     1 2 3   ")
    print("                     4 5 6   ")
    user = int(input("Choose your square : 7 8 9 : "))
    if user < 1 or user > 9:
        return get_player_move(board)
    row = (user - 1) // 3
    col = (user - 1) % 3
    if board[row][col] != " ":
        print("Invalid move.")
        return get_player_move(board)
    # and return row and col
    return row, col

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    computer = random.randint(1, 9)
    row = (computer - 1) // 3
    col = (computer - 1) % 3
    if board[row][col] != " ":
        return choose_computer_move(board)
    # and return row and col
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # check for diagonals
    if (board[0][0] == board[1][1] == board[2][2] == mark) or (board[2][0] == board[1][1] == board[0][2] == mark):
        return True
    # check for rows and columns
    for i in range(len(board)):
        if (board[i][0] == board[i][1] == board[i][2] == mark or board[0][i] == board[1][i] == board[2][i] == mark):
            return True
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set the board cells to all single spaces ' '
    initialise_board(board)
    # then draw the board
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    while True:
        print("Your turn.....")
        rp, cp = get_player_move(board)
        board[rp][cp] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            print("---------> You Win <---------")
            return 1
        elif check_for_draw(board):
            print("---------> Match has ended in a draw <---------")
            return 0
        else:
            print("Computer's turn.....")
            rc, cc = choose_computer_move(board)
            board[rc][cc] = "O"
            draw_board(board)
            if check_for_win(board, "O"):
                print("---------> You Lose <---------")
                return -1
            elif check_for_draw(board):
                print("---------> Match has ended in a draw <---------")
                return 0
    return 0
                    
                
def menu():
    # Prompt the user to ask what to do
    print("Enter one of the following options : ")
    print("1 - Play the game\n2 - Save your score in the leaderboard\n3 - Load and display the leaderboard\nq - End the program")
    choice = input("1, 2, 3 or q? : ")
    if choice not in ['1', '2', '3', 'q']:
        print("Invalid option")
        return menu()
    return choice

def load_scores():
    # Function to load the scores from the leaderboard file
    with open('leaderboard.txt', 'r') as file:
        leaders = json.load(file)  # Load the scores from the file using JSON
    return leaders  # Return the loaded scores as a dictionary

def save_score(score):
    #function to save the current score of the player
    name = input("Enter your name : ")
    with open('leaderboard.txt', 'r') as file:
        leaders = json.load(file)
    leaders[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)
    print("The score has been saved....")
    return


def display_leaderboard(leaders):
    # function to display the leaderboard 
    sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
    print("Leaderboard:")
    for name, score in sorted_leaders:
        print(f"{name} : {score}")
    pass