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
        lines = input_file.readlines()

    y = 0
    x = 0
    #lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    for line in lines:
        command, val = line.split()
        val = int(val)
        if command == "forward":
            x += val
        elif command == "down":
            y += val
        elif command == "up":
            y -= val

        print(f"new position: x = {x}, y = {y}")

    print(x * y)


def part_two():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    y = 0
    x = 0
    aim = 0
    #lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    for line in lines:
        command, val = line.split()
        val = int(val)
        #breakpoint()
        if command == "forward":
            x += val
            y += (aim * val)
        elif command == "down":
            aim += val
        elif command == "up":
            aim -= val

        print(f"new position: x = {x}, y = {y}, aim = {aim}")

    print(x * y)


if __name__ == "__main__":
    part_two()
