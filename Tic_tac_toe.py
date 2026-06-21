from random import randrange

def display_board(board):
    for r in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[r][0]}   |   {board[r][1]}   |   {board[r][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid range! Please pick a square between 1 and 9.")
                continue
                
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if (row, col) not in free_fields:
                print("That square is already occupied! Try another one.")
                continue
                
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def make_list_of_free_fields(board):
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_fields.append((r, c))
    return free_fields


def victory_for(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:  
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:  
            return True
            
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
        
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    
    if len(free_fields) > 0:
        random_index = randrange(len(free_fields))
        row, col = free_fields[random_index]
        board[row][col] = 'X'



board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

board[1][1] = 'X'

game_over = False

while not game_over:
    display_board(board)
    
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("You won!")
        game_over = True
        break
        
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("It's a tie!")
        game_over = True
        break

    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("The computer wins!")
        game_over = True
        break
        
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("It's a tie!")
        game_over = True
        break