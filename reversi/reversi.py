import sys
board = [[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '],
         ['1', '.', '.', '.', '.', '.', '.', '.', '.', ' '],
         ['2', '.', '.', '.', '.', '.', '.', '.', '.', ' '],
         ['3', '.', '.', '.', '.', '.', '.', '.', '.', ' '],
         ['4', '.', '.', '.', 'W', 'B', '.', '.', '.', ' '],
         ['5', '.', '.', '.', 'B', 'W', '.', '.', '.', ' '],
         ['6', '.', '.', '.', '.', '.', '.', '.', '.', ' '],
         ['7', '.', '.', '.', '.', '.', '.', '.', '.', ' '],
         ['8', '.', '.', '.', '.', '.', '.', '.', '.', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


# board = [[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '],
#          ['1', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
#          ['2', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
#          ['3', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
#          ['4', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', ' '],
#          ['5', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W', ' '],
#          ['6', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
#          ['7', 'W', 'W', 'W', 'W', 'W', '.', 'W', 'W', ' '],
#          ['8', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
#          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
def in_board(board):
    for i in range(9):
        luu_bien1 = ' '.join(board[i]).strip()
        print(luu_bien1)


def check_valid(turn):
    ls = ['.', 'W', 'B']
    valid_choices = []
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] != '.' and board[i][j] != turn:
                for x, y in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1],
                             [-1, -1], [-1, 0], [-1, 1]]:
                    t = 1
                    if board[i+x*t][j+y*t] == ".":
                        while board[i-x*t][j-y*t] != turn:
                            if board[i-x*t][j-y*t] == '.':
                                break
                            elif board[i-x*t][j-y*t] == ' ':
                                break
                            t = t + 1
                        if board[i-x*t][j-y*t] == turn:
                            if chr(j+y+96) + str(i+x) not in valid_choices:
                                valid_choices.append(chr(j+y+96) + str(i+x))
    in_board(board)
    # print(sorted(valid_choices))

    if len(valid_choices) == 0:
        # in_board()
        print('Play {} cannot play.'.format(turn))
    else:
        # in_board(valid_choices)
        print('Valid choices:', ' '.join(valid_choices))
        try:
            new_choice = input("Player {}: ".format(turn))
        except EOFError:
            sys.exit()
        while new_choice not in valid_choices:
            print("{}: Invalid choice".format(new_choice))
            print('Valid choices:', ' '.join(valid_choices))
            new_choice = input("Player {}: ".format(turn))

        row = ord(new_choice[1]) - 48
        col = ord(new_choice[0]) - 96

        board[row][col] = turn
        occupy(row, col, turn)


def check_end(turn):
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == '.':
                return False
    return True


def check_poin(board):

    p_w = 0
    p_b = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 'W':
                p_w = p_w + 1
            if board[i][j] == 'B':
                p_b = p_b + 1
    print('Player {} cannot play.'.format(turn))
    in_board(board)
    if turn == 'B':
        print('Player W cannot play.')
    else:
        print('Player B cannot play.')
    print("End of the game. W: {}, B: {}".format(p_w, p_b))
    if p_w > p_b:
        print("W wins.")
    elif p_b > p_w:
        print("B wins.")
    else:
        print("Draws.")


def occupy(row, col, turn):
    if board[row+1][col] == 'W' or board[row+1][col] == 'B':
        for i in range(row+1, 9):
            if board[i][col] == turn:
                for j in range(row, i):
                    board[j][col] = turn
                break
    if board[row][col+1] == 'W' or board[row][col+1] == 'B':
        for i in range(col+1, 9):
            if board[row][i] == turn:
                # board[8][8] = 's'
                # print(row, col, i)
                for j in range(col, i):
                    board[row][j] = turn
                    # print(row, j, turn)
                break
    if board[row-1][col] == 'W' or board[row-1][col] == 'B':
        for i in range(1, row-1):
            if board[row-i][col] == turn:
                for j in range(row-i, row):
                    board[j][col] = turn
                break
    if board[row][col-1] == 'W' or board[row][col-1] == 'B':
        for i in range(1, col-1):
            if board[row][col-i] == turn:
                for j in range(col-i, col):
                    board[row][j] = turn
                break

    if board[row-1][col-1] == 'W' or board[row-1][col-1] == 'B':
        for i in range(1, min(row, col)):
            if board[row-i][col-i] == turn:
                for j in range(i):
                    board[row-j][col-j] = turn
                break
    if board[row+1][col+1] == 'W' or board[row+1][col+1] == 'B':
        for i in range(1, 9-max(row, col)):
            if board[row+i][col+i] == turn:
                for j in range(i):
                    board[row+j][col+j] = turn
                break
    if board[row+1][col-1] == 'W' or board[row+1][col-1] == 'B':
        for i in range(1, min(9-row, col)):
            if board[row+i][col-i] == turn:
                for j in range(i):
                    board[row+j][col-j] = turn
                break
    if board[row-1][col+1] == 'W' or board[row-1][col+1] == 'B':
        for i in range(1, min(row, 9-col)):
            if board[row-i][col+i] == turn:
                for j in range(i):
                    board[row-j][col+j] = turn
                break


turn = 'B'
while check_end(turn) is False:

    check_valid(turn)
    if turn == 'W':
        turn = 'B'
    else:
        turn = 'W'
in_board(board)
check_poin(board)
