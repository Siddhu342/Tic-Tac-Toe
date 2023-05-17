from noughtsandcrosses import *

# Function to run the game
def main():
    # Initialize the game board
    board = [['1','2','3'],
            ['4','5','6'],
            ['7','8','9']]
    # Welcome message and instructions
    welcome(board)
    # Initialize the total score
    total_score = 0
    while True:
        # Display the menu and get user's choice
        choice = menu()
        # Play the game
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:', total_score)
        # Save the score to a file
        if choice == '2':
            save_score(total_score)
        # Load and display the leaderboard
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        # Quit the game
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return
# Program execution begins here
if __name__ == '__main__':
    main()
