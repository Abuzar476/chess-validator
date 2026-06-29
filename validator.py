def is_path_clear(start_pos, end_pos, board_state):
    x1, y1 = start_pos
    x2, y2 = end_pos

    step_x = 0
    if x2 > x1: step_x = 1
    elif x2 < x1: step_x = -1

    step_y = 0
    if y2 > y1: step_y = 1
    elif y2 < y1: step_y = -1

    curr_x = x1 + step_x
    curr_y = y1 + step_y

    while (curr_x, curr_y) != (x2, y2):
        if board_state.get((curr_x, curr_y)) != '--':
            return False
        curr_x += step_x
        curr_y += step_y

    return True

def is_valid_knight(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

def is_valid_rook(start, end, board_state):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    if dx != 0 and dy != 0:
        return False
    return is_path_clear(start, end, board_state)

def is_valid_bishop(start, end, board_state):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    if dx != dy:
        return False
    return is_path_clear(start, end, board_state)

def is_valid_queen(start, end, board_state):
    return is_valid_rook(start, end, board_state) or is_valid_bishop(start, end, board_state)

def is_valid_king(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return dx <= 1 and dy <= 1 and (dx + dy) > 0

def is_valid_pawn(start, end, piece, is_capture):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    direction = 1 if piece[0] == 'w' else -1
    start_rank = 2 if piece[0] == 'w' else 7

    if is_capture:
        return abs(dx) == 1 and dy == direction
    else:
        if dx != 0:
            return False
        if dy == direction:
            return True
        if y1 == start_rank and dy == 2 * direction:
            return True
        return False

def is_legal_move(piece, start, end, board_state, is_capture=False):
    piece_type = piece[1]

    if piece_type == 'N': return is_valid_knight(start, end)
    elif piece_type == 'R': return is_valid_rook(start, end, board_state)
    elif piece_type == 'B': return is_valid_bishop(start, end, board_state)
    elif piece_type == 'Q': return is_valid_queen(start, end, board_state)
    elif piece_type == 'K': return is_valid_king(start, end)
    elif piece_type == 'P': return is_valid_pawn(start, end, piece, is_capture)

    return False
