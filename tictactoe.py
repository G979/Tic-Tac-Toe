def draw_grid(grid):
    has_right_symbols = True
    if has_right_symbols:
        print("---------")
        print('|',   grid[0],  grid[1],  grid[2], '|')
        print('|',   grid[3],  grid[4],  grid[5], '|')
        print('|',   grid[6],  grid[7],  grid[8], '|')
        print("---------")
    else:
        print('Input had something other than just symbols')


def result(grid):
    if check_rows(grid) != -1:
        print(check_rows(grid))
        exit()
    elif check_columns(grid) != -1:
        print(check_columns(grid))
        exit()
    elif check_diagonals(grid) != -1:
        print(check_diagonals(grid))
        exit()
    elif check_for_tie(grid):
        print("Draw")
        exit()


def check_rows(grid):
    row_1 = grid[0] == grid[1] == grid[2] != " "
    row_2 = grid[3] == grid[4] == grid[5] != " "
    row_3 = grid[6] == grid[7] == grid[8] != " "
    if row_1:
        return f"{grid[0]} wins"
    elif row_2:
        return f"{grid[3]} wins"
    elif row_3:
        return f"{grid[6]} wins"
    else:
        return -1


def check_columns(grid):
    column_1 = grid[0] == grid[3] == grid[6] != " "
    column_2 = grid[1] == grid[4] == grid[7] != " "
    column_3 = grid[2] == grid[5] == grid[8] != " "
    if column_1:
        return f"{grid[0]} wins"
    elif column_2:
        return f"{grid[1]} wins"
    elif column_3:
        return f"{grid[2]} wins"
    else:
        return -1


def check_diagonals(grid):
    diagonal_1 = grid[0] == grid[4] == grid[8] != " "
    diagonal_2 = grid[2] == grid[4] == grid[6] != " "
    if diagonal_1:
        return f"{grid[0]} wins"
    elif diagonal_2:
        return f"{grid[2]} wins"
    else:
        return -1


def check_for_tie(grid):
    if " " not in grid:
        return True
    else:
        return False


def make_move(cell, x, y):
    if x + y == 2:
        if cell[0] == " ":
            cell[0] = player
            draw_grid(cell)
            return 1
        else:
            print("This cell is occupied! Choose another one!")
            return -1
    elif x + y == 3:
        if x == 1:
            if cell[1] == " ":
                cell[1] = player
                draw_grid(cell)
                return 1
            else:
                print("This cell is occupied! Choose another one!")
                return -1
        else:
            if cell[3] == " ":
                cell[3] = player
                draw_grid(cell)
                return 1
            else:
                print("This cell is occupied! Choose another one!")
                return -1
    elif x + y == 4:
        if x == 1:
            if cell[2] == " ":
                cell[2] = player
                draw_grid(cell)
                return 1
            else:
                print("This cell is occupied! Choose another one!")
                return -1
        elif x == 2:
            if cell[4] == " ":
                cell[4] = player
                draw_grid(cell)
                return 1
            else:
                print("This cell is occupied! Choose another one!")
                return -1
        else:
            if cell[6] == " ":
                cell[6] = player
                draw_grid(cell)
                return 1
            else:
                print("This cell is occupied! Choose another one!")
                return -1
    elif x + y == 5:
        if x == 2:
            if cell[5] == " ":
                cell[5] = player
                draw_grid(cell)
                return 1
            else:
                print("This cell is occupied! Choose another one!")
                return -1
        else:
            if cell[7] == " ":
                cell[7] = player
                draw_grid(cell)
                return 1
            else:
                print("This cell is occupied! Choose another one!")
                return -1
    else:
        if cell[8] == " ":
            cell[8] = player
            draw_grid(cell)
            return 1
        else:
            print("This cell is occupied! Choose another one!")
            return -1


def analyzer(x, y):
    if x.isnumeric() is False or y.isnumeric() is False:
        print("You should enter numbers!")
        return -1
    elif int(x) not in range(1, 4) or int(y) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return -1
    else:
        return -2


def xos(cur_sym):
    if cur_sym == "X":
        return "Y"
    else:
        return "X"


if __name__ == '__main__':
    player = ''
    x_counter = 0
    o_counter = 0
    player_x_turn = 1
    player_o_turn = 0
    board = [' ' for x in range(9)]
    draw_grid(board)    # print Board
    while True:
        row, col = input("Enter the coordinates: ").split()
        if analyzer(row, col) == -1:
            continue
        else:
            row, col = [int(row), int(col)]
            if player_x_turn > player_o_turn:
                player = 'X'
                player_o_turn += 2
                x_counter += 1
            elif player_o_turn > player_x_turn:
                player = 'O'
                player_x_turn += 2
                o_counter += 1
            make_move(board, row, col)
            result(board)

# # result(string)




