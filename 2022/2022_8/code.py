def part_one():
    with open('input.txt', 'r') as input_file:
        code_input = input_file.readlines()

    visible_count = 0
    for y, row in enumerate(code_input):
        row = row.strip()
        for x, char in enumerate(row):
            print(f"row = {row}, char = {char}, index = {x}")
            if is_visible_from_side(x, row):
                visible_count += 1
            elif is_visible_from_top_bottom(y, x, code_input):
                visible_count += 1

    print(visible_count)

def is_visible_from_top_bottom(y, x, code_input):
    if (y == 0) or (y == len(code_input) - 1):
        print("char is in the first row or last row")
        return True
    elif int(code_input[y][x]) > max([int(code_input[i][x]) for i in range(0, y)]):
        print(f"char {code_input[y][x]} is greater than anything before it in the column")
        return True
    elif int(code_input[y][x]) > max([int(code_input[i][x]) for i in range(y+1, len(code_input))]):
        print(f"char {code_input[y][x]} is greater than anything after it in the column")
        return True


def is_visible_from_side(index, row):
    if (index == 0) or (index == len(row) - 1):
        print("char is in the first column or last column")
        return True
    elif int(row[index]) > max([int(i) for i in row[:index]]):
        print(f"char {row[index]} is greater than anything before it in the row")
        return True
    elif int(row[index]) > max([int(i) for i in row[index+1:]]):
        print(f"char {row[index]} is greater than anything after it in the row")
        return True
    return False


def part_two():
    with open('input.txt', 'r') as input_file:
        code_input = input_file.readlines()

    max_score = 0
    for y, row in enumerate(code_input):
        row = row.strip()
        for x, char in enumerate(row):
            scenic_score = calculate_scenic_score(x, y, code_input)
            if scenic_score > max_score:
                max_score = scenic_score

    print(f"max_score = {max_score}")


def calculate_scenic_score(x, y, code_input):
    val = int(code_input[y][x])
    row = code_input[y].strip()
    print(f"calculating total score for x={x}, y={y}")
    print(f"val = {val}, row = {row}")

    score_up = calc_up(val, row, x, y, code_input)
    score_left = calc_left(val, row, x, y, code_input)
    score_down = calc_down(val, row, x, y, code_input)
    score_right = calc_right(val, row, x, y, code_input)

    total_score = score_up * score_left * score_down * score_right
    print(f"score is {(score_up, score_left, score_down, score_right)}")
    print(f"total_score is {total_score}\n")
    return total_score


def calc_down(val, row, x, y, code_input):
    """Calculate score down."""
    if y == len(code_input) - 1:
        # last row
        return 0

    score = 1
    i = 1
    while (y + i < len(code_input) - 1) and (int(code_input[y + i][x]) < val):
        print(f"comparing {code_input[y + i][x]} to {val}. Adding 1 to score")
        score += 1
        i += 1
    print(f"stopping down comparison, returning {score}")
    return score


def calc_up(val, row, x, y, code_input):
    """Calculate score up."""
    if y == 0:
        # first row
        return 0

    score = 1
    i = 1
    while (y - i > 0) and (int(code_input[y - i][x]) < val):
        print(f"comparing {code_input[y - i][x]} to {val}. Adding 1 to score")
        score += 1
        i += 1
    print(f"stopping up comparison, returning {score}")
    return score


def calc_right(val, row, x, y, code_input):
    """Calculate score right."""
    if x == len(row) - 1:
        # end of the row
        return 0

    score = 1
    i = 1
    while (x + i < len(row) - 1) and (int(row[x + i]) < val):
        print(f"comparing {row[x+i]} to {val}. Adding 1 to score")
        score += 1
        i += 1
    print(f"stopping right comparison, returning {score}")
    return score


def calc_left(val, row, x, y, code_input):
    """Calculate score left."""
    if x == 0:
        return 0

    score = 1
    i = 1
    while (x - i >= 1) and (int(row[x - i]) < val):
        print(f"comparing {row[x - i]} to {val}. Adding 1 to score")
        score += 1
        i += 1
    print(f"stopping left comparison, returning {score}")
    return score


if __name__ == "__main__":
    part_two()
