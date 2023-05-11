

def part_one():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    increases = -1
    prev_measurement = 0
    lines = [199,200,208,210,200,207,240,269,260,263]
    for line in lines:
        measurement = line  # int(line.strip())
        if measurement > prev_measurement:
            increases += 1
        print(f"measurement = {measurement}, prev_measurement = {prev_measurement}, increases = {increases}")
        prev_measurement = measurement

    print(increases)

def part_two():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
        lines = [int(line.strip()) for line in lines]

    increases = 0
    prev_sum = 500000000
    # lines = [199,200,208,210,200,207,240,269,260,263]
    breakpoint()
    for i, measurement in enumerate(lines):
        if i == len(lines) - 2:
            break
        sum = measurement + lines[i+1] + lines[i+2]
        if sum > prev_sum:
            increases += 1
        # print(f"sum = {sum}, prev_sum = {prev_sum}, increases = {increases}")
        prev_sum = sum

    print(f"total increases: {increases}")

if __name__ == "__main__":
    part_two()
