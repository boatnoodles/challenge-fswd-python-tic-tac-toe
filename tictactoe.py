import tictactoehelpers as hp

players_moves = hp.players_moves
winner = hp.winner
turns = hp.turns

######################################################


board = hp.make_board()

# GAME WILL CONTINUE IF NO ONE HAS WON YET
while winner == False:
    # GET CURRENT PLAYER
    current_player = hp.check_player_turn(turns)

    print(f"Player {current_player}\n =========")
    # GETS INPUT FROM PLAYER
    x = input("Enter your x-coordinate: ")
    y = input("Enter your y-coordinate: ")

    # CHECKS IF INPUT IS A NUMBER
    if not hp.check_if_number(x, y):
        print("Ye fool, gimme a number\n")
        winner == False
        continue

    # CONVERTS INPUT FROM A STR TO AN INT
    x = int(x)
    y = int(y)

    # CHECK IF INPUT IS IN RANGE
    if not hp.check_in_range(x, y):
        print("Ye fool, not in range\n")
        winner == False
        continue

    # CHECKS IF CELL IS EMPTY
    # Only allow if cell is empty, or else trigger input again
    if hp.check_empty_cell(x, y, board):
        # UPDATES BOARD
        hp.update_board(board, x, y, current_player)
        # STORES MOVES
        hp.store_moves(current_player, players_moves, x, y)
        # INCREMENTS TURN COUNTER
        turns += 1
    else:
        # INSULTS USER
        print("\nYe fool, spot taken, open your eyes WIDE\n")
        winner = False

    # DISPLAYS BOARD
    hp.display_board(board)
    # CHECKS IF END OF GAME
    winner = hp.check_thanus(current_player)

    if winner:
        print(
            f"====================================\n========= Good Game! {current_player} won =========\n====================================\n")

    elif turns == 9:
        print("======================================\n====== Good Game! It was a draw ======\n======================================\n")
        break
