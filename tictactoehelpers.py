winning_configs = (
    {(0, 1), (1, 1), (2, 1)},
    {(0, 0), (1, 0), (2, 0)},
    {(0, 2), (1, 2), (2, 2)},
    {(0, 0), (0, 1), (0, 2)},
    {(1, 0), (1, 1), (1, 2)},
    {(2, 0), (2, 1), (2, 2)},
    {(0, 0), (1, 1), (2, 2)},
    {(2, 0), (1, 1), (0, 2)})

players_moves = {"x": set(), "o": set()}
winner = False
turns = 0


def make_board():
    return [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]


def check_player_turn(turns):
    # Toggle players
    # return turns % 2 == 0 ? "x" : "o"
    return "x" if turns % 2 == 0 else "o"


def check_if_number(x, y):
    # Check if input is a digit
    return x.isdigit() and y.isdigit()


def check_in_range(x, y):
    return x in range(3) and y in range(3)


def check_empty_cell(x, y, board):
    # Todo check if cell is empty
    if board[y][x] == "-":
        return True
    return False


def update_board(board, x, y, current_player):
    board[y][x] = current_player


def store_moves(current_player, players_moves, x, y):
    # SAVE PLAYERS' MOVES IN TWO SEPARATE SETS
    players_moves[current_player].add((y, x))
    return players_moves


def display_board(board):
    # Makes a clone of the board and displays it
    display_board = board[:]
    display_board.reverse()
    print("\n")
    for row in display_board:
        print(row)
    print("\n")


def check_thanus(current_player):
    # CHECK FOR WINNER
    for config in winning_configs:
        if config.issubset(players_moves[current_player]):
            return True
    return False
