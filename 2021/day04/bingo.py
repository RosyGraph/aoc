def print_boards(boards):
    for board in boards:
        print_board(board)
        print()


def print_board(board):
    print("\n".join(map(str, board)))


def init_bingo():
    boards = []
    drawn_numbers = []
    with open("in/2.in", "r") as f:
        drawn_numbers = map(int, f.readline().split(","))
        i = 0
        board = []
        for line in f.readlines()[1:]:
            line = line.rstrip()
            if not line:
                continue
            board.append([[int(x), False] for x in line.rstrip().split()])
            if i == 4:
                boards.append(board)
                board = []
            i = (i + 1) % 5
    return (boards, drawn_numbers)


def play(boards, drawn_numbers):
    won = [False for _ in boards]
    for n in drawn_numbers:
        for b, board in enumerate(boards):
            for row in board:
                for e in row:
                    if n == e[0]:
                        e[1] = True
                        if not won[b] and check_win(board):
                            won[b] = True
                        if all(won):
                            return board, n
    return [], -1


def check_win(board):
    # check rows
    for row in board:
        if row[0][1]:
            if all(x[1] for x in row[1:]):
                return True
    # check columns
    for i, e in enumerate(board[0]):
        if e[1]:
            if all([row[i][1] for row in board]):
                return True
    return False


if __name__ == "__main__":
    boards, drawn_numbers = init_bingo()
    board, n = play(boards, drawn_numbers)
    print(n * sum(sum(x[0] for x in row if not x[1]) for row in board))
