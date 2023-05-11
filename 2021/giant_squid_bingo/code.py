import math
from pprint import pprint


def part_one():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    draws = lines.pop(0).strip().split(',')

    total_boards = create_boards(lines)

    # draw numbers for bingo
    for num in draws:
        print(f"Drawing number ... {num}")
        win = ['X'] * 5
        for board in total_boards:
            for i, row in enumerate(board):
                if num in row:
                    # replace the number with an X to mark it as called
                    board[i] = ['X' if elem == num else elem for elem in row]
                    if board[i] == win:
                        return calculate_final_score(board, num)


def create_boards(lines):
    """
    Parse lines of input and return a list of bingo boards.
    """
    num_boards = math.floor(len(lines) / 6)
    lines = "".join(lines).split('\n')
    boards = []
    for i in range(num_boards):
        # split lines into boards of 5 rows each
        if lines[0] == "":
            lines.pop(0)
        boards.append(lines[:5])
        lines = lines[5:]

    # create duplicate boards for vertical bingos
    vert_boards = []
    for board in boards:
        vert_board = []
        vert_board.append(" ".join([row[:2] for row in board]))
        vert_board.append(" ".join([row[3:5] for row in board]))
        vert_board.append(" ".join([row[6:8] for row in board]))
        vert_board.append(" ".join([row[9:11] for row in board]))
        vert_board.append(" ".join([row[12:14] for row in board]))

        vert_boards.append(vert_board)

    total_boards = boards + vert_boards
    for board in total_boards:
        for i, row in enumerate(board):
            # transform rows to lists of single integers
            board[i] = [num for num in row.split(' ') if num != ""]

    return total_boards


def calculate_final_score(board, last_num_drawn):
    """
    Find sum of all unmarked numbers, then multiply by last num drawn.
    """
    pprint(board)
    # flatten list to one array
    all_numbers = [num for row in board for num in row]
    # transform to ints, or 0 if num crossed out
    all_numbers = [int(num) if num != 'X' else 0 for num in all_numbers]
    board_sum = sum(all_numbers)
    # multiply sum by the number that was called to create the win
    return board_sum * int(last_num_drawn)


def part_two():
    # with open('input.txt', 'r') as input_file:
    #     lines = input_file.readlines()

    print("NYI")


if __name__ == "__main__":
    score = part_one()
    print(f"Final score is ... {score}")
