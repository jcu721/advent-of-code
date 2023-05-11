drawn_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
boards = [
"22 13 17 11  0",
 "8  2 23  4 24",
"21  9 14 16  7",
 "6 10  3 18  5",
 "1 12 20 15 19",

 "3 15  0  2 22",
 "9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",

"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
 "2  0 12  3  7",
]

board_1 = [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12,  3, 7]]


def has_win(board):
    breakpoint()
    diagonals = [[], []]
    columns = [[],[],[],[],[]]
    for i in range(len(board)):
        print(f"i={i}")
        for j in range(len(board)):
            print(f"j={j}")
            columns[i].append(board[i][j])
            print(columns)

        # columns.append(col)
        diagonals[0].append(board[i][i])
        diagonals[1].append(board[i][4-i])

    breakpoint()
    possibilities = columns + diagonals + board
    for x in possibilities:
        if x == [-1, -1, -1, -1, -1]:
            return True

    # [1][1], [2][1], [3][1]
    # vertical_wins = [board[x][y] for x in range(len(board)-1) for y in range(len(board)-1)]

    # for row in boards:
    #     if len(row):
    #         pass


def part_one():
    # with open('input.txt', 'r') as input_file:
    #     lines = input_file.readlines()
    boards = boards 
    for draw in drawn_numbers:
        mark_boards(draw)
        for board in boards:
            if has_win(board):
                print(f"board {board} has a win")
                

def mark_boards(number):
    pass

if __name__ == "__main__":
    has_win(board_1)