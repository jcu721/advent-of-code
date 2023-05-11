input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def part_one():
    with open('input.txt', 'r') as input_file:
        all_fish = input_file.readlines()

    all_fish = [3, 4, 3, 1, 2]

    for i in range(1, 18):
        new_fish = []
        for fish_age in all_fish:
            if fish_age == 0:
                new_fish.append(8)
            else:
                fish_age -= 1
        all_fish.append(new_fish)
        print(all_fish)

    print(len(all_fish))


def part_two():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()


if __name__ == "__main__":
    part_one()
