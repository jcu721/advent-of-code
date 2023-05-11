import math

def part_one():
    with open('input.txt', 'r') as input_file:
        rucksacks = input_file.readlines()

    chars = []
    for rucksack in rucksacks:
        center_index = math.floor(len(rucksack)/2)
        first_half = rucksack[:center_index]
        second_half = rucksack[center_index:]

        for char in first_half:
            if char in second_half:
                print(f"first_half = {first_half}")
                print(f"char = {char}")
                chars.append(char)
                break

    sum = 0
    for x in chars:
        if ord(x) > 96:
            sum += ord(x) - 96
        else:
            sum += ord(x) - 38

    print(sum)


def part_two():
    with open('input.txt', 'r') as input_file:
        rucksacks = input_file.readlines()

    # rucksacks = [
    #     "vJrwpWtwJgWrhcsFMMfFFhFp",
    #     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #     "PmmdzqPrVvPwwTWBwg",
    #     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #     "ttgJtRGJQctTZtZT",
    #     "CrZsJsPPZsGzwwsLwLmpwMDw"
    # ]
    chars = []
    num_groups = math.floor(len(rucksacks)/3)
    for i in range(0, num_groups):
        first = rucksacks[i*3]
        second = rucksacks[i*3+1]
        third = rucksacks[i*3+2]

        print(first)
        print(second)
        print(third)
        for char in first:
            if char in second and char in third:
                print(f"char = {char}")
                chars.append(char)
                break

    sum = 0
    for x in chars:
        if ord(x) > 96:
            sum += ord(x) - 96
        else:
            sum += ord(x) - 38

    print(sum)

if __name__ == "__main__":
    part_two()
