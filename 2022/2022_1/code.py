

def part_one():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    calorie_list = []
    current_calorie_load = 0
    for line in lines:
        # breakpoint()
        if line.strip() == '':
            calorie_list.append(current_calorie_load)
            current_calorie_load = 0
        else:
            current_calorie_load += int(line.strip())

    print(max(calorie_list))

def part_two():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    calorie_list = []
    current_calorie_load = 0
    for line in lines:
        # breakpoint()
        if line.strip() == '':
            calorie_list.append(current_calorie_load)
            current_calorie_load = 0
        else:
            current_calorie_load += int(line.strip())

    top_three = 0
    breakpoint()
    top_three += max(calorie_list)
    calorie_list.remove(max(calorie_list))
    top_three += max(calorie_list)
    calorie_list.remove(max(calorie_list))
    top_three += max(calorie_list)
    calorie_list.remove(max(calorie_list))

    print(top_three)

if __name__ == "__main__":
    part_two()
