from math import floor

def part_one():
    with open('input.txt', 'r') as input_file:
        all_fish = input_file.readlines()
        all_fish = [int(fish) for fish in all_fish[0].split(',')]

    # all_fish = [3, 4, 3, 1, 2]

    for _days in range(0, 256):
        print(_days)
        new_fish = []
        for i, fish_age in enumerate(all_fish):
            if fish_age == 0:
                new_fish.append(8)
                all_fish[i] = 6
            else:
                all_fish[i] = fish_age - 1
        if len(new_fish) > 0:
            all_fish.extend(new_fish)
        # print(all_fish)

    print(len(all_fish))

# tree = [
# 1    "1, 2, 3, 4, 5, 6",
# 2    "0, 1, 2, 3, 4, 5",
# 3    "6, 0, 1, 2, 3, 4, 8",
# 4    "5, 6, 0, 1, 2, 3, 7, 8",
# 5    "4, 5, 6, 0, 1, 2, 6, 7, 8",
# 6    "3, 4, 5, 6, 0, 1, 5, 6, 7, 8",
# 7    "2, 3, 4, 5, 6, 0, 4, 5, 6, 7, 8",
# 8    "1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8",
# 9    "0, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7",
# 10   "6, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 8",
# 11   "5, 6, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 7, 8",
# 12   "4, 5, 6, 0, 1, 2, 6, 0, 1, 2, 3, 4, 6, 7, 8, 8",
# ]

# another tree = [
# 1    "0, 1, 2, 3, 4, 5, 6",
# 2    "6, 0, 1, 2, 3, 4, 5, 8",
# 3    "5, 6, 0, 1, 2, 3, 4, 7, 8",
# 4    "4, 5, 6, 0, 1, 2, 3, 6, 7, 8",
# 5    "3, 4, 5, 6, 0, 1, 2, 5, 6, 7, 8",
# 6    "2, 3, 4, 5, 6, 0, 1, 4, 5, 6, 7, 8",
# 7    "1, 2, 3, 4, 5, 6, 0, 3, 4, 5, 6, 7, 8",
# 8    "0, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7, 8",
# 9    "6, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8",
# 10   "5, 6, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8",
# 11   "4, 5, 6, 0, 1, 2, 3, 6, 0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 8",
# 12   "3, 4, 5, 6, 0, 1, 2, 5, 6, 0, 1, 2, 3, 4, 6, 7, 7, 8, 8, 8, 8",
# ]
example_tree = [
    "1, 2, 3, 3, 4",
    "0, 1, 2, 3, 3",
    "6, 0, 1, 1, 2, 8",
    "5, 6, 0, 0, 1, 7, 8",
]

# every single day there will be at least one respawn
# one for loop over the number of days

"""
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,`8
After  5 days: 5,6,5,3,4,5,6,7,7,``8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,`8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,``8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,`8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,`8,``8,8,8
"""
TOTAL_DAYS = 256


def part_two():
    with open('input.txt', 'r') as input_file:
        all_fish = input_file.readlines()
        all_fish = [int(fish) for fish in all_fish[0].split(',')]

    # all_fish = [3, 4, 3, 1, 2]
    fish_counts = [all_fish.count(i) for i in range(0, 9)]

    for day in range(0, TOTAL_DAYS):
        zeros = fish_counts[0]
        ones = fish_counts[1]
        twos = fish_counts[2]
        threes = fish_counts[3]
        fours = fish_counts[4]
        fives = fish_counts[5]
        sixes = fish_counts[6]
        sevens = fish_counts[7]
        eights = fish_counts[8]

        fish_counts[0] = ones
        fish_counts[1] = twos
        fish_counts[2] = threes
        fish_counts[3] = fours
        fish_counts[4] = fives
        fish_counts[5] = sixes
        fish_counts[6] = sevens + zeros
        fish_counts[7] = eights
        fish_counts[8] = zeros

        # print(f"new fish_counts = {fish_counts}")
        # print(f"total fish = {sum(fish_counts)}")

    print(f"final number of fish = {sum(fish_counts)}")


def part_two_fail():
    with open('input.txt', 'r') as input_file:
        all_fish = input_file.readlines()
        all_fish = [int(fish) for fish in all_fish[0].split(',')]

    all_fish = [3, 4, 3, 1, 2]

    new_fish = 0
    for i, fish_age in enumerate(all_fish):
        # print(f"fish i={i}, age={fish_age}")
        # breakpoint()
        # how many fish will each fish create in it's lifetime of 256 days
        respawns = calculate_respawns(fish_age, TOTAL_DAYS, 0)
        print(respawns)
        new_fish += respawns

    print(new_fish + len(all_fish))


def calculate_respawns(fish_age, days_remaining, days_elapsed):
    if days_remaining >= 0:
        print(f"calculating respawns for fish age = {fish_age}, days_remaining = {days_remaining}, days_elapsed = {days_elapsed}")
    else:
        print(f"calculating respawns for fish age = {fish_age}, days_remaining = {days_remaining}")
    if days_remaining < fish_age:
        print("there is not enough time for the fish to respawn")
        return 0
    else:
        # return the number of new fish this one will respawn
        num_spawned_fish = floor((days_remaining - (fish_age + 1)) / 7) + 1
        print(f"num_spawned_fish = {num_spawned_fish}")
        total = num_spawned_fish
        initial_spawn_remaining_days = days_remaining - fish_age - 1
        for fish_num in range(0, num_spawned_fish):
            remaining_days_for_spawn = initial_spawn_remaining_days - (fish_num * 7)
            days_elapsed = TOTAL_DAYS - remaining_days_for_spawn
            total += calculate_respawns(8, remaining_days_for_spawn, days_elapsed)

        print(f"total added = {total}")
        return total


if __name__ == "__main__":
    part_two()
