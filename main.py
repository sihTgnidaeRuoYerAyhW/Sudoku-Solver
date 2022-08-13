board = [[0, 0, 5, 0, 0, 7, 0, 0, 2],
        [2, 0, 4, 0, 0, 0, 9, 0, 0],
        [9, 6, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 0],
        [7, 0, 0, 2, 4, 1, 0, 0, 6],
        [0, 0, 0, 0, 5, 9, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 6, 8],
        [0, 0, 7, 0, 0, 0, 2, 0, 9],
        [1, 0, 0, 4, 0, 0, 7, 0, 0]]


def possible(i,j,number):
    if number in board[i]:
        return False
    if number in [row[j] for row in board]:
        return False
    x = (i//3)*3
    y = (j//3)*3
    for x_off in [0, 1, 2]:
        for y_off in [0, 1, 2]:
            if number == board[x + x_off][y + y_off]:
                return False
    return True


def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1,10):
                    if possible(i,j,n):
                        board[i][j] = n
                        solve()
                        board[i][j] = 0
                return
    for row in board:
        print(row)


solve()