def setup_board():
    board = {}
    # White pieces
    board[(1,1)] = 'wR'
    board[(2,1)] = 'wN'
    board[(3,1)] = 'wB'
    board[(4,1)] = 'wQ'
    board[(5,1)] = 'wK'
    board[(6,1)] = 'wB'
    board[(7,1)] = 'wN'
    board[(8,1)] = 'wR'
    # White pawns
    for i in range(1, 9):
        board[(i,2)] = 'wP'
    # Black pieces
    board[(1,8)] = 'bR'
    board[(2,8)] = 'bN'
    board[(3,8)] = 'bB'
    board[(4,8)] = 'bQ'
    board[(5,8)] = 'bK'
    board[(6,8)] = 'bB'
    board[(7,8)] = 'bN'
    board[(8,8)] = 'bR'
    # Black pawns
    for i in range(1, 9):
        board[(i,7)] = 'bP'
    # Empty squares
    for x in range(1, 9):
        for y in range(3, 7):
            board[(x,y)] = '--'
    return board

def print_board(board):
    print("\n  a  b  c  d  e  f  g  h")
    for y in range(8, 0, -1):
        row_str = str(y) + " "
        for x in range(1, 9):
            row_str += board[(x,y)] + " "
        print(row_str + " " + str(y))
    print("  a  b  c  d  e  f  g  h\n")

if __name__ == "__main__":
    my_board = setup_board()
    print_board(my_board)
