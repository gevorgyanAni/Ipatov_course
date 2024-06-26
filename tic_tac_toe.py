def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, mark):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # строки
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # столбцы
        [0, 4, 8], [2, 4, 6]  # диагонали
    ]
    for combo in win_combinations:
        if all(board[i] == mark for i in combo):
            return True
    return False


def is_full(board):
    return all(cell in ["X", "O"] for cell in board)


def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    while True:
        print_board(board)
        move = int(input(f"Игрок {current_player}, выберите ячейку (1-9): ")) - 1

        if board[move] in ["X", "O"]:
            print("Ячейка уже занята! Попробуйте еще раз.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} выиграл!")
            break

        if is_full(board):
            print_board(board)
            print("Ничья!")
            break

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
