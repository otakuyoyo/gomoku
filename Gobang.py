def initialize_board(size=15):
    return [[' ' for _ in range(size)] for _ in range(size)]

def colored_piece(piece):
    if piece == 'X':
        return f"\033[91m{piece}\033[0m"  # Red
    elif piece == 'O':
        return f"\033[92m{piece}\033[0m"  # Green
    return piece

def print_board(board):
    size = len(board)
    # Print the top column numbers
    print("    " + " ".join(f"{i+1:2}" for i in range(size)))
    print("  +" + "---+" * size)
    for idx, row in enumerate(board):
        print(f"{idx+1:2} | " + " | ".join(colored_piece(cell) for cell in row) + " |")
        print("  +" + "---+" * size)

def check_winner(board, player):
    size = len(board)
    # Check horizontal, vertical, and diagonal lines
    for row in range(size):
        for col in range(size):
            if board[row][col] == player:
                # Check horizontal
                if col + 4 < size and all(board[row][col+i] == player for i in range(5)):
                    return True
                # Check vertical
                if row + 4 < size and all(board[row+i][col] == player for i in range(5)):
                    return True
                # Check diagonal (down-right)
                if row + 4 < size and col + 4 < size and all(board[row+i][col+i] == player for i in range(5)):
                    return True
                # Check diagonal (down-left)
                if row + 4 < size and col - 4 >= 0 and all(board[row+i][col-i] == player for i in range(5)):
                    return True
    return False

def play_game():
    board = initialize_board()
    print("歡迎來到五子棋遊戲！")
    print("玩家1: 黑子 (X) \033[91m紅色\033[0m")
    print("玩家2: 白子 (O) \033[92m綠色\033[0m")
    current_player = 'X'  # X starts the game, representing black stones
    while True:
        print_board(board)
        print(f"玩家 {current_player} 的回合")
        try:
            row = int(input("請輸入行 (1-15): ")) - 1
            col = int(input("請輸入列 (1-15): ")) - 1
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == ' ':
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"玩家 {current_player} 獲勝！")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("無效的移動，請重試。")
        except ValueError:
            print("請輸入有效的數字。")

if __name__ == "__main__":
    play_game()
