import board
import translator
import validator

def play_game():
    print("=== Welcome to the Terminal Chess Validator ===")
    print("Type 'quit' at any prompt to exit the game.\n")

    game_board = board.setup_board()
    current_turn = 'w'

    while True:
        board.print_board(game_board)

        turn_name = "White" if current_turn == 'w' else "Black"
        print(f"--- {turn_name}'s Turn ---")

        start_input = input("Enter the piece you want to move (e.g., e2): ").strip()
        if start_input.lower() == 'quit':
            print("Game ended by user.")
            break

        end_input = input("Enter the destination (e.g., e4): ").strip()
        if end_input.lower() == 'quit':
            print("Game ended by user.")
            break

        try:
            start_coord = translator.coords(start_input)
            end_coord = translator.coords(end_input)
        except (ValueError, KeyError, IndexError):
            print("❌ Invalid input format! Please use standard coordinates like 'e2'.")
            continue

        piece = game_board.get(start_coord)
        if piece is None or piece == '--':
            print("❌ There is no piece on that square! Try again.")
            continue

        if piece[0] != current_turn:
            print(f"❌ That is not your piece! It is {turn_name}'s turn.")
            continue

        destination_piece = game_board.get(end_coord)
        is_capture = False

        if destination_piece is None:
            print("❌ Invalid destination square!")
            continue

        if destination_piece != '--':
            if destination_piece[0] == current_turn:
                print("❌ You cannot capture your own piece!")
                continue
            is_capture = True

        if validator.is_legal_move(piece, start_coord, end_coord, game_board, is_capture):
            game_board[end_coord] = piece
            game_board[start_coord] = '--'
            print("✅ Move accepted!")
            current_turn = 'b' if current_turn == 'w' else 'w'
        else:
            print(f"❌ Illegal move for a {piece}! Try again.")

if __name__ == "__main__":
    play_game()
