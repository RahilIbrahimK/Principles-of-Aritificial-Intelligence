board = [" " for _ in range(9)]

def print_board():
    print("-------------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3+1], "|", board[i*3+2], "|")
        print("-------------")

def check_win(player):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_tie():
    return " " not in board

def reset_game():
    global board
    board = [" " for _ in range(9)]

print("Welcome to Tic Tac Toe!")
print_board()

while True:
    x = int(input("Enter the position you want to place your X (1-9): "))
    if board[x-1] == " ":
        board[x-1] = "X"
        print_board()
        if check_win("X"):
            print("X wins!")
            reset_game()
        elif check_tie():
            print("It's a tie!")
            reset_game()
        else:
            o = int(input("Enter the position you want to place your O (1-9): "))
            if board[o-1] == " ":
                board[o-1] = "O"
                print_board()
                if check_win("O"):
                    print("O wins!")
                    reset_game()
                elif check_tie():
                    print("It's a tie!")
                    reset_game()
            else:
                print("That position is already taken!")
    else:
        print("That position is already taken!")
    