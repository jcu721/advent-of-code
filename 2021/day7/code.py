def part_one(starting_positions):
    cost_array = []
    for position in range(0, max(starting_positions)):
        cost_array = cost_array + [calculate_fuel_cost(position, starting_positions)]

    print(f"min cost = {min(cost_array)}")


def calculate_fuel_cost(final_position, position_array):
    fuel_cost = 0
    for crab in position_array:
        fuel_cost += abs(crab - final_position)

    # print(f"fuel cost = {fuel_cost} for final_position = {final_position}")
    return fuel_cost


def part_two(starting_positions):
    cost_array = []

    for position in range(0, max(starting_positions)):
        cost_array = cost_array + [calculate_increasing_fuel_cost(position, starting_positions)]

    print(f"min cost = {min(cost_array)}")


def calculate_increasing_fuel_cost(final_position, position_array):
    fuel_cost = 0
    for crab in position_array:
        total_steps = abs(crab - final_position)
        cost = sum([i for i in range(0, total_steps + 1)])
        fuel_cost += cost

    # print(f"fuel cost = {fuel_cost} for final_position = {final_position}")
    return fuel_cost


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        input = input_file.readlines()
        # input = ['16,1,2,0,4,2,7,1,2,14']
        positions = [int(x) for x in input[0].split(',')]
    part_two(positions)
