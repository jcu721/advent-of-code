weight_map = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3,  # scissors
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}
# rock beats scissors, paper beats rock, scissors beat paper
# 1 beats 3, 2 beats 1, 3 beats 2
# 1, 2, 3, 1
beats_map = {
    1: 3,
    2: 1,
    3: 2,
}

def part_one():
    with open('input.txt', 'r') as input_file:
        games = input_file.readlines()

    total_score = 0
    for game in games:
        (opponent, you) = game.strip().split()
        total_score += calculate_score(opponent, you)

    print(total_score)

def calculate_score(opponent, you):
    # could do this in python 10 with the match statement
    score = 0

    score += weight_map[you]
    if weight_map[opponent] == weight_map[you]:  # draw
        score += 3
    elif beats_map[weight_map[opponent]] == weight_map[you]:  # you lose
        score += 0
    else:  # you win
        score += 6

    return score


def part_two():
    with open('input.txt', 'r') as input_file:
        games = input_file.readlines()

    # X means you need to lose
    # Y means you need to draw
    # Z means you need to win

    total_score = 0
    for game in games:
        (opponent, you) = game.strip().split()
        total_score += calculate_choice(opponent, you)

    print(total_score)
    # should get 12

def calculate_choice(opponent, you):
    # rock beats scissors, paper beats rock, scissors beat paper
    # 1 beats 3, 2 beats 1, 3 beats 2 
    # 1, 2, 3, 1
    beats_map = {
        1: 3, 
        2: 1, 
        3: 2,
    }
    reverse_map = {
        1: "X",  # rock
        2: "Y",  # paper
        3: "Z",  # scissors
    }

    if you == "X":  # you need to lose
        return calculate_score(opponent, reverse_map[beats_map[weight_map[opponent]]])
    elif you == "Y":  # you need to draw
        # choose the same symbol as your opponent
        return calculate_score(opponent, opponent)
    else:  # you == "Z", you need to win
        # choose the item that beats your opponent
        winning_symbol = [symbol for symbol in beats_map if beats_map[symbol] == weight_map[opponent]]
        return calculate_score(opponent, reverse_map[winning_symbol[0]])


if __name__ == "__main__":
    part_two()
