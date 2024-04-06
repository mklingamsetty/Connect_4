def print_board(board):
    for k in range(len(board)):
        for l in range(len(board[k])):
            print(board[k][l], end = " ")
        print()
def initialize_board(num_rows, num_cols):
    board = [["-" for i in range(num_cols)] for j in range(num_rows)]
    return board

def insert_chip(board, col, chip_type):
    for i in range(len(board)-1, -1, -1):
        if(board[i][col] == ('-') and board[i][col] != 'x' and board[i][col] != 'o'):
            board[i][col] = chip_type
            return i
        elif(i == 0):
            return 0
        else:
            continue

def check_if_winner(board, col, row, chip_type):
    #player scores
    score = 0

    #checks player score
    for i in range(len(board)):
        if(board[i][col] == chip_type):
            score += 1

    if(score < 4):
        score = 0

    for j in range(len(board[0])):
        if(board[row][j] == chip_type):
            score += 1

    if(score < 4):
        score = 0

    #checks if current player won
    if(score >= 4):
        return True
    else:
        return False


def main():
    check = True

    rows = int(input("What would you like the height of the board to be?"))
    columns = int(input("What would you like the length of the board to be?"))
    newBoard = initialize_board(rows, columns)
    print_board(newBoard)

    print("Player 1: x\nPlayer 2: o")
    counter = 0
    while check:
        if (counter%2 == 0):
            columnPlacement = int(input("\nPlayer 1: Which column would you like to choose? "))
            chip_type = 'x'
            rowPlacement = insert_chip(newBoard, columnPlacement, chip_type)
            #print("rowPlacement: ", rowPlacement)
            print_board(newBoard)
        else:
            columnPlacement = int(input("\nPlayer 2: Which column would you like to choose? "))
            chip_type = 'o'
            rowPlacement = insert_chip(newBoard, columnPlacement, chip_type)
            #print("rowPlacement: ", rowPlacement)
            print_board(newBoard)


        if(check_if_winner(newBoard, columnPlacement, rowPlacement, chip_type) == True):
            if(counter%2 == 0):
                print("\nPlayer 1 won the game!")
            else:
                print("\nPlayer 2 won the game!")

            check = False

        counter += 1

        if (any('-' in sublist for sublist in newBoard)):
            continue
        else:
            print("\nDraw. Nobody wins.")
            check = False

if __name__ == "__main__":
    main()